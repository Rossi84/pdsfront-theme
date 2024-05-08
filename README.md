# Portale delle segnalazioni FRONT docs theme

This is the official theme for any piece of documentation of Portale delle segnalazioni.

## How to use Sphinx CW theme on your documentation

* Add the following line to your documentation `requirements.txt` file:

    ```
    $ pip install git+https://github.com/Rossi84/pdsfront-theme.git
    ```

* In your `conf.py` file, you'll need to specify the theme as follows:

    ```
    # Add this line at the top of the file within the "import" section
    import pdsfront_theme

    # Add the Sphinx extension 'pdsfront_theme' in the extensions list
    extensions = [
      ...,
      'pdsfront_theme'
    ]

    # Edit these lines
    html_theme = "pdsfront_theme"
    html_theme_path = [pdsfront_theme.get_html_theme_path()]
    ```