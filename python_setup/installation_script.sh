#!/bin/bash

# Script to install packages from pacman, yay, and set up yay if not installed
# Define alias for pacman
alias sps='sudo pacman -S --noconfirm'

# Log file for installation process
LOG_FILE="$HOME/package_installation.log"
echo "Starting package installation at $(date)" >"$LOG_FILE"

# Function to log messages
log_message() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check and install yay if not present
install_yay() {
  if command_exists yay; then
    log_message "yay is already installed"
    return 0
  fi

  log_message "yay not found, installing yay..."

  # Install base-devel and git if not present
  sps base-devel git >>"$LOG_FILE" 2>&1 || {
    log_message "ERROR: Failed to install base-devel and git"
    exit 1
  }

  # Clone yay repository
  cd /tmp || {
    log_message "ERROR: Failed to change to /tmp directory"
    exit 1
  }

  git clone https://aur.archlinux.org/yay.git >>"$LOG_FILE" 2>&1 || {
    log_message "ERROR: Failed to clone yay repository"
    exit 1
  }

  cd yay || {
    log_message "ERROR: Failed to enter yay directory"
    exit 1
  }

  # Build and install yay
  makepkg -si --noconfirm >>"$LOG_FILE" 2>&1 || {
    log_message "ERROR: Failed to build and install yay"
    exit 1
  }

  cd ~ || {
    log_message "ERROR: Failed to return to home directory"
    exit 1
  }

  log_message "yay installed successfully"
}

# Install pacman packages
install_pacman_packages() {
  log_message "Installing pacman packages..."
  local packages=(
    "kitty hyprshot neovim"
    "ark"
    "neofetch"
    "kate"
    "gammastep"
    "npm rust"
    "go rust"
    "pyenv"
    "python"
    "tree"
    "opencv"
    "fd"
    "lazygit"
    "sddm qt5-graphicaleffects qt5-quickcontrols2 qt5-svg"
    "qt5-quickcontrols2 qt5-graphicaleffects qt5-svg"
    "git" # Adding git as requested
    "fish"
    "fzf"
    "lynx"
    "github-cli"
    "okular"
    "gcc"
    "g++"
    "swaylock"
    "gtk3"
    "gtk4"
    "gtklock"
  )

  for pkg in "${packages[@]}"; do
    log_message "Installing pacman package(s): $pkg"
    sps $pkg >>"$LOG_FILE" 2>&1 || log_message "WARNING: Failed to install $pkg"
  done
}

# Install yay packages
install_yay_packages() {
  log_message "Installing yay packages..."
  local packages=(
    "brave-bin"
    "wlogout swaylock-effects"
    "sddm-sugar-candy-git"
  )

  for pkg in "${packages[@]}"; do
    log_message "Installing yay package(s): $pkg"
    yay -S --noconfirm $pkg >>"$LOG_FILE" 2>&1 || log_message "WARNING: Failed to install $pkg"
  done
}

# Main execution
log_message "Starting package installation script"

# Update system first
log_message "Updating system..."
sudo pacman -Syu --noconfirm >>"$LOG_FILE" 2>&1 || {
  log_message "ERROR: Failed to update system"
  exit 1
}

# Install yay if needed
install_yay

# Install all packages
install_pacman_packages
install_yay_packages

log_message "Package installation completed at $(date)"
echo "Installation complete. Check $LOG_FILE for details."
