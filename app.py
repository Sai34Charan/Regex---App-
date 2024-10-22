from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_regex():
    """Process the regex matching request."""
    input_string = request.form.get('test_string', '')
    regex = request.form.get('regex', '')

    matches = []
    error_message = None
    
    try:
        # Attempt to find all matches in the input string
        matches = re.findall(regex, input_string)
    except re.error:
        error_message = "Invalid Regex Pattern"

    # Prepare the context for rendering
    context = {
        'input_string': input_string,
        'regex': regex,
        'matches': matches if matches else None,
        'error_message': error_message,
        'no_matches_message': "No matches found" if not matches and not error_message else None
    }
    
    return render_template('index.html', **context)

@app.route('/email_validation')
def email_validation_page():
    """Render the email validation page."""
    return render_template('email.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    """Validate the provided email address."""
    email_address = request.form.get('email', '')
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid_email = re.match(email_pattern, email_address) is not None

    return render_template('email.html', email=email_address, is_valid=is_valid_email)

if __name__ == '__main__':
    app.run(debug=True)