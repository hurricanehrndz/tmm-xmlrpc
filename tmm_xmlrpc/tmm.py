import subprocess


class tmm(object):
    def __init__(self, executable):
        self.executable = executable

    def update(self):
        """TinyMediaManager update sources."""
        update_result = subprocess.run([self.executable, '-update'])
        if update_result.returncode == 0:
            return True
        return False

    def scrape_unscraped(self):
        """TinyMediaManager scrape unscraped."""
        scraper_results = subprocess.run([self.executable, '-scrapeUnscraped'])
        if scraper_results.returncode == 0:
            return True
        return False

    def rename(self):
        rename_results = subprocess.run([self.executable, '-rename'])
        if rename_results.returncode == 0:
            return True
        return False
