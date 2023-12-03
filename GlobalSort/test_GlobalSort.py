from GlobalSort import sort_files, main
from unittest.mock import patch
from pathlib import Path
import unittest
import os
import shutil


def generate_menu(language):
    # Define the menu options in each language
    menus = {
        "en": {
            "Music": "Music",
            "Videos": "Videos",
            "Images": "Images",
            "Documents": "Documents",
            "Downloads": "Downloads",
        },
        "fr": {
            "Music": "Musique",
            "Videos": "Vidéos",
            "Images": "Images",
            "Documents": "Documents",
            "Downloads": "Téléchargements",
        },
        "de": {
            "Music": "Musik",
            "Videos": "Videos",
            "Images": "Bilder",
            "Documents": "Dokumente",
            "Downloads": "Downloads",
        },
        "es": {
            "Music": "Música",
            "Videos": "Videos",
            "Images": "Imágenes",
            "Documents": "Documentos",
            "Downloads": "Descargas",
        },
        "it": {
            "Music": "Musica",
            "Videos": "Video",
            "Images": "Immagini",
            "Documents": "Documenti",
            "Downloads": "Download",
        },
        "ru": {
            "Music": "Музыка",
            "Videos": "Видео",
            "Images": "Изображения",
            "Documents": "Документы",
            "Downloads": "Загрузки",
        },
    }

    # Get the menu in the selected language
    menu = menus.get(language)

    # Return the menu as a string
    return "\n".join(f"{i+1}. {option}" for i, option in enumerate(menu.values()))


class TestSortFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = Path("test_dir")
        self.test_dir.mkdir(exist_ok=True)

        # Create a test file in the directory
        self.test_file = self.test_dir / "test_file.txt"
        self.test_file.touch()

    def tearDown(self):
        # Clean up the test directory after each test
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_sort_files_existing_extension(self):
        # Define a simple extension map for testing
        extensions = {".txt": "Text Files"}

        # Call the function with the test directory and extension map
        sort_files(self.test_dir, extensions)

        # Check that the file has been moved to the correct directory
        self.assertTrue((self.test_dir / "Text Files" / "test_file.txt").exists())

    def test_sort_files_non_existing_extension(self):
        # Define a simple extension map for testing
        extensions = {".doc": "Documents"}

        # Call the function with the test directory and extension map
        sort_files(self.test_dir, extensions)

        # Check that the file has been moved to the 'Divers' directory
        self.assertTrue((self.test_dir / "Divers" / "test_file.txt").exists())

    def test_sort_files_non_existing_directory(self):
        # Define a simple extension map for testing
        extensions = {".txt": "Text Files"}

        # Call the function with a non-existing directory and extension map
        sort_files(Path("non_existing_dir"), extensions)

        # Check that the file has not been moved
        self.assertTrue(self.test_file.exists())

    def test_main_menu(self):
        # Mock the input function to simulate user input
        with patch("builtins.input", side_effect=["1", "9"]):
            try:
                # Call the main function
                main()
            except SystemExit:
                pass

    def test_sort_files_existing_file(self):
        # Define a simple extension map for testing
        extensions = {".txt": "Text Files"}

        # Create a file in the target directory
        target_dir = self.test_dir / "Text Files"
        target_dir.mkdir(exist_ok=True)
        target_file = target_dir / "test_file.txt"
        target_file.touch()

        # Call the function with the test directory and extension map
        sort_files(self.test_dir, extensions)

        # Check that the original file has been removed
        self.assertFalse(self.test_file.exists())

        # Check that the file in the target directory still exists
        self.assertTrue(target_file.exists())


class TestGenerateMenu(unittest.TestCase):
    def test_generate_menu_english(self):
        expected_menu = "1. Music\n2. Videos\n3. Images\n4. Documents\n5. Downloads"
        self.assertEqual(generate_menu("en"), expected_menu)

    def test_generate_menu_french(self):
        expected_menu = (
            "1. Musique\n2. Vidéos\n3. Images\n4. Documents\n5. Téléchargements"
        )
        self.assertEqual(generate_menu("fr"), expected_menu)

    def test_generate_menu_german(self):
        expected_menu = "1. Musik\n2. Videos\n3. Bilder\n4. Dokumente\n5. Downloads"
        self.assertEqual(generate_menu("de"), expected_menu)

    def test_generate_menu_spanish(self):
        expected_menu = "1. Música\n2. Videos\n3. Imágenes\n4. Documentos\n5. Descargas"
        self.assertEqual(generate_menu("es"), expected_menu)

    def test_generate_menu_italian(self):
        expected_menu = "1. Musica\n2. Video\n3. Immagini\n4. Documenti\n5. Download"
        self.assertEqual(generate_menu("it"), expected_menu)

    def test_generate_menu_russian(self):
        expected_menu = "1. Музыка\n2. Видео\n3. Изображения\n4. Документы\n5. Загрузки"
        self.assertEqual(generate_menu("ru"), expected_menu)


if __name__ == "__main__":
    unittest.main()
