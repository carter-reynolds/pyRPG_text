from textwrap import wrap as wrap_text
     
 
def make_text_box(title="", text="", choices=[""]):
    
    """ 
    This function is used to display a text box in the terminal.
        
    _arguments_
     
    title: The title of the text box (String)
    text: The text that will be displayed in the text box (String)
    choices: A list of choices that the user can select from (List of Strings)
    
    """ 
    
    # Setup unicode characters for the box
    chars = {
        'a': '┌',
        'b': '┐',
        'c': '┘',
        'd': '└',
        'e': '─',
        'f': '│',
        'g': '┴',
        'h': '├',
        'i': '┬',
        'j': '┤',
        'k': '╷',
        'l': '┼',
    }
    
    # Setup the areas of the box that will be filled with unicode characters
    top_left_corner = chars['a']
    top_right_corner = chars['b']
    bottom_right_corner = chars['c']
    bottom_left_corner = chars['d']
    top = chars['e']
    bottom = chars['e']
    left = chars['f']
    right = chars['f']
    line_width = 60
    
    # Wrap the text to fit the width of the box - add indents to the wrapped text
    text = wrap_text(text, line_width, initial_indent='    ', subsequent_indent='    ')
    
    # List of lengths of each line of text
    line_sizes = []
    
    # Append the length of each line of text to the list
    for line in text:
        line_sizes.append(len(line))
    
    # Find the longest line of text and add some padding around it    
    max_line_size = max(line_sizes)
    max_line_size += 4
    
    # Print the title of the box if one was passed
    print(f"{title}")
    
    # Print the top of the box
    top_box = top_left_corner + (top * max_line_size) + top_right_corner
    print(f"{top_box}")
    
    # For each line of text, draw the left side of the box, the text, and the right side of the box
    for line in text:
        remaining_space = line_width - len(line)
        print(f"{left}{line}{' ' * (remaining_space-5)}{right}")
    
    # Print the bottom of the box    
    print(left + (top * max_line_size) + right)
    
    # Print the choices that the user can select from    
    for choice in choices:
        print(f"{left}{choice}{' ' * (max_line_size - len(choice))}{right}")
        
    # Draw the bottom of the box    
    print(f"{bottom_left_corner}{bottom * max_line_size}{bottom_right_corner}")

     

    