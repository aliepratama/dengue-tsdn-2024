from flask import render_template
from werkzeug.exceptions import NotFound


def get_404(e: NotFound | None = None) -> tuple[str, int]:
    """
    Handles 404 Not Found errors by rendering a custom 404 error page.
    Args:
        e (NotFound | None): The exception that triggered the 404 error, if any.
    Returns:
        tuple[str, int]: A tuple containing the rendered HTML for the 404 error page and the HTTP status code 404.
    """
    return render_template('404.html', error=str(e)), 404
