import os

def take_screenshot(driver, test_name):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    filename = f"{test_name}.png"
    filepath = os.path.join(screenshots_dir, filename)

    try:
        driver.save_screenshot(filepath)
        print(f"[✓] Screenshot alındı: {filepath}")
    except Exception as e:
        print(f"[!] Screenshot alınamadı: {e}")
