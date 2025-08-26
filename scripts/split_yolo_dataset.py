import os
import random
import shutil
import argparse
from pathlib import Path

# === CONFIGURATION ===
SPLIT_SIZE = 2000
TRAIN_RATIO = 0.8
DATASET_PREFIX = "dataset_split"


# === Step 1: Collect all image-label pairs ===
def find_valid_pairs(image_dirs, label_dirs):
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp"}
    label_extensions = set()
    all_labels = set()

    for label_dir in label_dirs:
        for f in os.listdir(label_dir):
            ext = os.path.splitext(f)[1].lower()
            if ext == ".txt":
                label_extensions.add(ext)
                all_labels.add(os.path.splitext(f)[0])

    valid_pairs = []
    unmatched_images = []

    for image_dir in image_dirs:
        for img_file in os.listdir(image_dir):
            name, ext = os.path.splitext(img_file)
            ext = ext.lower()
            if ext in image_extensions:
                label_file = name + ".txt"
                label_path = next(
                    (
                        label_dir / label_file
                        for label_dir in label_dirs
                        if (label_dir / label_file).exists()
                    ),
                    None,
                )
                if label_path:
                    valid_pairs.append((image_dir / img_file, label_path))
                else:
                    unmatched_images.append(image_dir / img_file)

    return valid_pairs, unmatched_images


# === Step 2: Create splits ===
def create_split_folder(base_out, pairs):
    train_size = int(len(pairs) * TRAIN_RATIO)
    train_pairs = pairs[:train_size]
    val_pairs = pairs[train_size:]

    folders = {
        "train/images": [],
        "train/labels": [],
        "valid/images": [],
        "valid/labels": [],
    }

    for img, lbl in train_pairs:
        folders["train/images"].append(img)
        folders["train/labels"].append(lbl)
    for img, lbl in val_pairs:
        folders["valid/images"].append(img)
        folders["valid/labels"].append(lbl)

    for subfolder, files in folders.items():
        dest = base_out / subfolder
        dest.mkdir(parents=True, exist_ok=True)
        for src in files:
            shutil.copy(src, dest)

    # Generate data.yaml
    yaml_path = base_out / "data.yaml"
    with open(yaml_path, "w") as f:
        f.write("train: train/images\n")
        f.write("val: valid/images\n")
        f.write("nc: 1\n")
        f.write("names: ['License_Plate']\n")


# === Step 3: Main logic ===
def main():
    parser = argparse.ArgumentParser(
        description="Split YOLOv8 dataset into multiple training sets."
    )
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Path to YOLOv8 dataset directory (with train/ valid/ test/)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=".",
        help="Directory where split datasets will be saved",
    )
    args = parser.parse_args()

    source_dir = Path(args.source)
    output_dir = Path(args.output)

    train_dir = source_dir / "train"
    valid_dir = source_dir / "valid"
    test_dir = source_dir / "test"

    image_dirs = [train_dir / "images", valid_dir / "images", test_dir / "images"]
    label_dirs = [train_dir / "labels", valid_dir / "labels", test_dir / "labels"]

    print("🔍 Scanning dataset...")
    pairs, unmatched = find_valid_pairs(image_dirs, label_dirs)

    print(f"✅ Found {len(pairs)} valid image-label pairs.")
    print(f"⚠️ Found {len(unmatched)} images without matching labels.")

    if unmatched:
        print(f"🗑 Deleting {len(unmatched)} unmatched images...")
        for img in unmatched:
            img.unlink()

    random.shuffle(pairs)

    # === Dynamically calculate number of full 2000-sized splits ===
    num_full_splits = len(pairs) // SPLIT_SIZE
    leftover_count = len(pairs) % SPLIT_SIZE

    print(f"🔢 Total full splits possible: {num_full_splits}")
    print(f"📦 Leftover image-label pairs: {leftover_count}")

    # === Create full split folders ===
    for i in range(num_full_splits):
        start = i * SPLIT_SIZE
        end = start + SPLIT_SIZE
        split_pairs = pairs[start:end]
        folder = output_dir / f"{DATASET_PREFIX}_{i + 1}"
        print(f"📂 Creating {folder} with {len(split_pairs)} pairs...")
        create_split_folder(folder, split_pairs)

    # === Handle leftover ===
    # leftover = pairs[num_full_splits * SPLIT_SIZE :]
    # if leftover:
    #     if len(leftover) > 3000:
    #         # Make one more full split folder if leftover is large
    #         folder = output_dir / f"{DATASET_PREFIX}_{num_full_splits + 1}"
    #         print(
    #             f"📂 Creating extra full split (large leftover) with {len(leftover)} pairs..."
    #         )
    #         create_split_folder(folder, leftover)
    #     else:
    #         # Place leftover in a smaller split folder
    #         folder = output_dir / f"{DATASET_PREFIX}_leftover"
    #         print(f"📂 Creating leftover folder with {len(leftover)} pairs...")
    #         create_split_folder(folder, leftover)
    # else:
    #     print("✅ No leftover pairs remaining.")
    # === Handle leftover ===
    leftover = pairs[num_full_splits * SPLIT_SIZE :]
    if leftover:
        if len(leftover) > 1500:
            # Create new folder for leftover
            folder = output_dir / f"{DATASET_PREFIX}_{num_full_splits + 1}"
            print(
                f"📂 Creating extra split (large leftover) with {len(leftover)} pairs..."
            )
            create_split_folder(folder, leftover)
        else:
            # Merge leftover into the last full split folder
            folder = output_dir / f"{DATASET_PREFIX}_{num_full_splits}"
            print(
                f"🔄 Merging leftover ({len(leftover)} pairs) into last split: {folder.name}"
            )
            # Append leftover to that folder
            existing_folder_pairs = pairs[
                (num_full_splits - 1) * SPLIT_SIZE : num_full_splits * SPLIT_SIZE
            ]
            combined = existing_folder_pairs + leftover
            # Remove original folder contents and recreate it fully
            shutil.rmtree(folder)
            create_split_folder(folder, combined)
    else:
        print("✅ No leftover pairs remaining.")

    # for i in range(4):
    #     start = i * SPLIT_SIZE
    #     end = start + SPLIT_SIZE
    #     split_pairs = pairs[start:end]
    #     if len(split_pairs) < SPLIT_SIZE:
    #         print(f"🚫 Not enough pairs for split {i + 1}. Skipping.")
    #         break
    #     folder = output_dir / f"{DATASET_PREFIX}_{i + 1}"
    #     print(f"📦 Creating {folder} with {len(split_pairs)} pairs...")
    #     create_split_folder(folder, split_pairs)
    #
    # leftover = pairs[4 * SPLIT_SIZE :]
    # if leftover:
    #     folder = output_dir / f"{DATASET_PREFIX}_leftover"
    #     print(f"📦 Creating leftover folder with {len(leftover)} pairs...")
    #     create_split_folder(folder, leftover)
    # else:
    #     print("✅ No leftover pairs remaining.")


if __name__ == "__main__":
    main()
