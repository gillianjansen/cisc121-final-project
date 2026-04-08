# project code

def library_binary_search(bookshelf, target_book):
    # this performs a binary search to find a target book in an alphabetically-ordered bookshelf
    # parameters:
        # bookshelf (list): a sorted list of book titles (string)
        # target_book (str): the title of the ook the user is looking for
    # returns:
        # str: a step-by-step log of the search process to display in the ui

    search_log = f"Searching for: '{target_book}'\n" # going to build a log so that the user can see updates on what the search is doing
    search_log += "-" * 40 + "\n"

    if not target_book.strip(): # for if the user clicks search without typing anything
        return "Please enter a book title to search for."

    low = 0 # low is index of first book in the list/search range
    high = len(bookshelf) - 1 # high is the index of the last book

    while low <= high: # search as long as low has not crossed high index
        mid = (low + high) // 2  # find the exact middle of the list using floor division
        current_book = bookshelf[mid]

        search_log += f"Checking the middle of the current section (Index {mid}). \n"
        search_log += f"The middle book is: '{current_book}'. \n"

        target_lower = target_book.lower() # converting everything to lowercase in the event that the user types in "Title" and/or "title"
        current_lower = current_book.lower()

        # option 1. middle is the book
        if current_lower == target_lower:
            search_log += f"Success! We found '{current_book}'. \n"
            return search_log # we found it, so we stop the function and return the log

        # option 2. target book comes alphabetically after the current book
        elif current_lower < target_lower:
            search_log += f"'{target_book}' comes after '{current_book}' alphabetically. \n"
            search_log += "Ignoring left half of the shelf. \n\n"
            low = mid + 1 # moving the low index up past the middle book (cuz we already searched the middle index)

        # option 3. target book comes alphabetically before the current book
        else:
            search_log += f"'{target_book}' comes before '{current_book}' alphabetically. \n"
            search_log += "Ignoring right half of the shelf. \n\n"
            high = mid - 1 # moving the high index down past the middle

    search_log += "Search complete. The book is not currently on this shelf." # this is if the loop finishes and we haven't returned the success message (aka the book isnt there)
    return search_log

# alphabetized library shelf
library_shelf = [
    "1984", "Animal Farm", "Blood of Elves", "Caraval", "Charlotte's Web",
    "Clockwork Angel", "Frankenstein", "Hamlet", "Harry Potter and the Philosopher's Stone",
    "Lord of the Flies", "The Fellowship of the Ring", "Pride and Prejudice",
    "Prince Caspian", "Rebecca", "Six of Crows", "Strange the Dreamer",
    "The Boys in the Boat", "The Count of Monte Cristo", "The Goldfinch",
    "The Great Gatsby", "The Handmaid's Tale", "The Keeper of Lost Causes",
    "The Secret History", "To Kill a Mockingbird", "Ulysses", "War and Peace"
]

library_shelf.sort() # resort list if things are added

# gradio

import gradio as gr
gr.close_all()
import time

# alphabetized library shelf
library_shelf = [
    "1984", "Animal Farm", "Blood of Elves", "Caraval", "Charlotte's Web",
    "Clockwork Angel", "Frankenstein", "Hamlet", "Harry Potter and the Philosopher's Stone",
    "Lord of the Flies", "The Fellowship of the Ring", "Pride and Prejudice",
    "Prince Caspian", "Rebecca", "Six of Crows", "Strange the Dreamer",
    "The Boys in the Boat", "The Count of Monte Cristo", "The Goldfinch",
    "The Great Gatsby", "The Handmaid's Tale", "The Keeper of Lost Causes",
    "The Secret History", "To Kill a Mockingbird", "Ulysses", "War and Peace"
]

def generate_html_shelf(low_idx, high_idx, mid_idx=None, is_found=False):
    # helper function creates HTML visual of bookshelf
    # dims books outside of search range and highlights middle book

    # start a container that wraps the books nicely like a grid
    html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; font-family: sans-serif;'>"

    for i, book in enumerate(library_shelf):
        # default styling for books currently in our active search range
        bg_color = "#e2e8f0"      # light gray background
        text_color = "#000000"    # black text
        opacity = "1.0"           # fully visible
        border = "1px solid #cbd5e1"

        # 1. dim the books we have discarded
        if i < low_idx or i > high_idx:
            opacity = "0.2"       # make them faded

        # 2. highlight the "middle" book we are currently checking
        elif i == mid_idx:
            if is_found:
                bg_color = "#22c55e" # green if we found it
                text_color = "white"
            else:
                bg_color = "#fbbf24" # yellow while we are checking it
                text_color = "black"
                border = "2px solid #b45309"

        # build the HTML block for this specific book
        book_div = f"<div style='padding: 8px 12px; border-radius: 6px; background-color: {bg_color}; color: {text_color}; opacity: {opacity}; border: {border}; font-size: 14px;'>{book}</div>"
        html += book_div

    html += "</div>"
    return html

def animated_binary_search(target_book):
    # binary search algorithm but with visual updates
    if not target_book.strip():
        yield "<h3 style='color:red;'> Please type a book name first!</h3>"
        return

    target_lower = target_book.lower()
    low = 0
    high = len(library_shelf) - 1
    step_count = 1

    # show the initial full shelf before starting the math
    status_text = f"<h3> Starting search for: '{target_book}'...</h3>"
    yield generate_html_shelf(0, len(library_shelf)-1) + status_text
    time.sleep(1.5) # pause for 1.5 seconds so the user can read the text

    while low <= high:
        mid = (low + high) // 2
        current_book = library_shelf[mid]

        # animation frame 1: highlight the middle book we are checking
        status_text = f"<h3> Step {step_count}: Pulling the middle book (Index {mid})... It is '{current_book}'.</h3>"
        yield generate_html_shelf(low, high, mid_idx=mid, is_found=False) + status_text
        time.sleep(2) # pause so the user can see the yellow highlight

        if current_book.lower() == target_lower:
            # animation frame: success
            status_text += f"<h3 style='color: green;'>Success! '{current_book}' matches our target! Click 'Reset' to Search for another Book.</h3>"
            yield generate_html_shelf(low, high, mid_idx=mid, is_found=True) + status_text
            return

        elif current_book.lower() < target_lower:
            status_text += f"<h3> '{target_book}' comes AFTER '{current_book}'. Discarding the left half...</h3>"
            # update boundaries
            low = mid + 1
        else:
            status_text += f"<h3> '{target_book}' comes BEFORE '{current_book}'. Discarding the right half...</h3>"
            # update boundaries
            high = mid - 1

        #  text explaining the math before moving to the next loop
        yield generate_html_shelf(low, high) + status_text
        time.sleep(2)
        step_count += 1

    # animation frame: failure (aka book not found)
    status_text = "<h3 style='color: red;'>Search complete. The book is not on this shelf.</h3>"
    yield generate_html_shelf(low, high) + status_text


def reset_ui(): # resets ui to og state
    return "", generate_html_shelf(0, len(library_shelf)-1) + "<h3>Ready to search. Type a book above.</h3>"


# gradio interface setup

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Library Book Finder (Binary Search Visualization)")
    gr.Markdown("Type a book from the list below to see how a computer finds it using Binary Search. Take note of how it halves the shelf every step.")

    with gr.Row():
        # user input box
        book_input = gr.Textbox(label="Target Book Title", placeholder="e.g. Rebecca")

    with gr.Row():
        # buttons
        search_btn = gr.Button("Search", variant="primary")
        reset_btn = gr.Button("Reset")

    # output box (using HTML so colorful CSS divs render correctly)
    visual_output = gr.HTML(generate_html_shelf(0, len(library_shelf)-1) + "<h3>Ready to search! Type a book above.</h3>")

    # connect the buttons to our python functions
    search_btn.click(fn=animated_binary_search, inputs=book_input, outputs=visual_output)
    reset_btn.click(fn=reset_ui, inputs=[], outputs=[book_input, visual_output])

# launch the app
if __name__ == "__main__":
    demo.launch()
