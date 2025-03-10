import webbrowser

def multiply_and_play():
    """
    Prompts the user for the result of 1 * 1. If correct, opens a video.
    """
    while True:
        try:
            user_input = int(input("1 times 1 = ? "))
            if user_input == 1:
                play_video()
                break
            else:
                print("Wrong! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_video():
    """
    Opens a video link in the web browser.
    """
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(video_url)
    print("Playing video...")

if __name__ == "__main__":
    multiply_and_play()
