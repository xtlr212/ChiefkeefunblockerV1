import webbrowser

def open_html_with_about_blank(html_file_path):
    url = "about:blank"
    webbrowser.open_new_tab(url)

    # You can add your HTML file path here to open it in a separate tab
    webbrowser.open_new_tab("file://" + chiefkeefunblockerV1.html)

if __name__ == "__main__":
    html_file_path = "chiefkeefunblockerV1.html"
    open_html_with_about_blank(html_file_path)
