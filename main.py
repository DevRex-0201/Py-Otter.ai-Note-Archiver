from playwright.sync_api import sync_playwright
import time
import datetime

url = "https://otter.ai/signin"

def download_and_delete_notes(page):
    # Navigate to the notes page
    page.goto("https://otter.ai/my-notes")
    time.sleep(10)

    # Loop through available notes
    while True:
        note = page.query_selector(".conversation-list-item")
        if not note:
            print("All notes have been exported.")
            break

        a_tag = note.query_selector("a")
        note_link = "https://otter.ai" + a_tag.get_attribute("href")
        page.goto(note_link)
        time.sleep(10)

        # Extract and format the note title for use as the filename
        title_element = page.query_selector("#conversation-header-relative-time")
        if title_element:
            title = title_element.inner_text()
            extra = title.split(", ")[0] + ", "
            title = title.replace(extra, "")
            date = title.split(" .")[0]
            date = datetime.datetime.strptime(date, "%b %d, %Y").strftime("%m-%d-%Y")
            title = date + " " + title.split(" . ")[1]
        else:
            title = "Untitled Note"

        # Initiate note download
        page.click('[aria-label="Edit Note"]')
        time.sleep(1)
        page.fill(".otter-editor__content-editor", title)
        time.sleep(1)
        page.click(".mat-tooltip-trigger.head-bar__menu-button")
        time.sleep(1)
        export_option = page.query_selector(".local-options-menu").query_selector_all("li")[2]
        export_option.click()
        time.sleep(2)

        # Handle the download
        with page.expect_download() as download_info:
            page.click("#export-panel-button-complete")
            download = download_info.value
            download.save_as(download.suggested_filename)
        time.sleep(5)

        # Delete the note after downloading
        page.click(".mat-tooltip-trigger.head-bar__menu-button")
        delete_option = page.query_selector(".local-options-menu").query_selector_all("li")[-1]
        delete_option.click()
        time.sleep(1)
        page.click("#single-confirm-overlay-primary-action")
        time.sleep(5)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context("browser_data", headless=False)
        page = browser.new_page()
        page.goto(url)
        
        input("Please login to your Otter account, and then press Enter to continue...")

        try:
            download_and_delete_notes(page)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            page.close()
            browser.close()

if __name__ == "__main__":
    main()
