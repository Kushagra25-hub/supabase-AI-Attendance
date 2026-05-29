# SnapClass 🎓

SnapClass is an AI-powered smart attendance system built using Streamlit that automates attendance using Face Recognition and Voice Recognition.

## Features

- Face-based student login
- Voice-based attendance support
- Teacher portal
- Student portal
- Subject enrollment
- Attendance tracking
- Dashboard analytics
- AI-based identity verification

## Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- WebRTC VAD
- Face Recognition
- Machine Learning
- SQLite / Database

## Project Structure

```
SnapClass/
│
├── app.py
├── requirements.txt
├── src/
│   ├── components/
│   ├── screens/
│   ├── pipelines/
│   ├── database/
│   └── ui/
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd SnapClass
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
streamlit run app.py
```

## Usage

1. Open the application
2. Register as Student or Teacher
3. Login using Face ID
4. Enroll in subjects
5. Track attendance

## Future Improvements

- QR attendance support
- Email notifications
- Cloud deployment
- Advanced analytics

## Author

Kushagra
