# My Best Voting System 😎
# A mini project to let users vote for their favorite candidate using loops, if/else, and a dictionary!

# Storing our awesome candidates in a dictionary with their vote counts
candidates = {
    "Emma Watson": 0,
    "Liam Chen": 0,
    "Ava Rodriguez": 0,
    "Noah Patel": 0,
    "Sophia Kim": 0
}

# Voting Menu - Let's make it fun!
def display_menu():
    print("\n=== Welcome to Our Epic Voting Booth ===")
    print("Choose your favorite candidate to vote for:")
    for i, candidate in enumerate(candidates.keys(), 1):
        print(f"{i}. {candidate}")
    print("0. Exit and see results")

# Vote for Candidate - Tally those votes!
def vote_for_candidate():
    while True:
        display_menu()
        choice = input("\nEnter the number of your candidate (0 to exit): ")
        
        # Check if the user wants to exit
        if choice == "0":
            print("\n=== Voting Closed! Here’s the Final Tally ===")
            show_results()
            break
        
        # Validate the input
        if choice.isdigit() and 1 <= int(choice) <= len(candidates):
            selected_candidate = list(candidates.keys())[int(choice) - 1]
            candidates[selected_candidate] += 1
            print(f"\n🎉 Vote cast for {selected_candidate}! Keep the vibes going! 🎉")
        else:
            print("\nOops, that’s not a valid choice! Try again, homie!")

# Show Results - Who’s winning our election?
def show_results():
    print("\n=== Election Results ===")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} vote(s)")
    
    # Find the winner (or winners in case of a tie)
    max_votes = max(candidates.values())
    winners = [candidate for candidate, votes in candidates.items() if votes == max_votes]
    
    if max_votes == 0:
        print("\nNo votes were cast. Y’all sleeping on this election? 😴")
    elif len(winners) > 1:
        print("\nIt’s a tie! The following candidates are neck and neck:")
        for winner in winners:
            print(f"- {winner} with {max_votes} vote(s)")
    else:
        print(f"\n🏆 The winner is {winners[0]} with {max_votes} vote(s)! 🏆")

# Main Program - Let’s get this party started!
print("Welcome to My Best Voting System! Let’s elect a legend! 🚀")
vote_for_candidate()
