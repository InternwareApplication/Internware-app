# In your database setup or seed script
from app.repositories.user import UserRepository
from app.repositories.student import StudentRepository
from app.database import get_cli_session

with get_cli_session() as session:
    user_repo = UserRepository(session)
    student_repo = StudentRepository(session)
    
    # Create bob user (student role)
    bob = user_repo.create(
        username="bob",
        email="bob@internware.com",
        password="bobpass",
        role="student"
    )
    
    # Create student profile
    student_repo.create(
        user_id=bob.id,
        name="Bob Smith",
        major="Computer Science",
        gpa=3.8,
        skills="Python, React, SQL",
        graduation_year=2027
    )