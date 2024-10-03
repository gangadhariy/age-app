from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def new_func():
    if request.method == 'POST':
        age = request.form.get('age')

        if not age:
            return render_template_string(HTML_FORM, result="Please enter a valid age")
        elif age.isalpha():
            return render_template_string(HTML_FORM, result="Please enter a valid numeric age.")
        else:
            age = int(age)
            if age < 13:
                result = "Child: He should be in school"
            elif age <= 18:
                result = "Teenager: He should be in college"
            else:
                result = "Adult: He should be in a job or business"

            return render_template_string(HTML_FORM, result=result)
    
    return render_template_string(HTML_FORM)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Age Category</title>
    <style>
        body {
            background-color: #f0f8ff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }
        .form-container {
            background: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            font-size: 40px;
            font-weight: bold;
            text-transform: uppercase;
            color: #333;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        label {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            display: block;
        }
        input[type="text"] {
            width: 80%;
            padding: 10px;
            margin-bottom: 20px;
            font-size: 18px;
            border-radius: 8px;
            border: 1px solid #ccc;
            box-shadow: inset 0px 0px 10px rgba(0, 0, 0, 0.05);
        }
        .submit-btn {
            background-color: #4CAF50;
            color: white;
            padding: 15px 25px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            box-shadow: 0 4px #999;
        }
        .submit-btn:hover {
            background-color: #45a049;
        }
        .submit-btn:active {
            background-color: #3e8e41;
            box-shadow: 0 2px #666;
            transform: translateY(2px);
        }
        .result {
            margin-top: 20px;
            font-size: 22px;
            font-weight: bold;
            color: #333;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

    <div class="form-container">
        <h1>Age Category</h1>
        <form method="POST">
            <label for="age">Enter your age:</label>
            <input type="text" id="age" name="age" placeholder="Enter age here">
            <input type="submit" value="Submit" class="submit-btn">
        </form>
        <p class="result">{{ result }}</p>
    </div>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
