from django.core.management.base import BaseCommand
from certificates.models import Student, Certificate
from datetime import date


class Command(BaseCommand):
    help = 'Load sample students and certificates for testing'

    def handle(self, *args, **options):
        samples = [
            {
                "student_id": "155049",
                "name": "Dhruv Patel",
                "email": "dhruv.patel@example.com",
                "mobile": "9876543210",
                "course": "Full Stack Web Development",
                "batch": "2025-A",
                "cert_id": "ITC-CERT-2025-155049",
                "course_name": "Full Stack Web Development Internship",
                "duration": "3 Months (July - September 2025)",
                "grade": "A+",
            },
            {
                "student_id": "155050",
                "name": "Priya Shah",
                "email": "priya.shah@example.com",
                "mobile": "9876543211",
                "course": "Python Programming",
                "batch": "2025-A",
                "cert_id": "ITC-CERT-2025-155050",
                "course_name": "Python Programming & Django",
                "duration": "2 Months",
                "grade": "A",
            },
            {
                "student_id": "155051",
                "name": "Rahul Mehta",
                "email": "rahul.mehta@example.com",
                "mobile": "9876543212",
                "course": "Data Science Basics",
                "batch": "2025-B",
                "cert_id": "ITC-CERT-2025-155051",
                "course_name": "Data Science Fundamentals",
                "duration": "3 Months",
                "grade": "A+",
            },
            {
                "student_id": "155052",
                "name": "Ananya Desai",
                "email": "ananya.desai@example.com",
                "mobile": "9876543213",
                "course": "UI/UX Design",
                "batch": "2025-B",
                "cert_id": "ITC-CERT-2025-155052",
                "course_name": "UI/UX Design Internship",
                "duration": "2 Months",
                "grade": "A",
            },
        ]

        self.stdout.write("Loading sample data...\n")

        for s in samples:
            student, created = Student.objects.update_or_create(
                student_id=s["student_id"],
                defaults={
                    "name": s["name"],
                    "email": s["email"],
                    "mobile": s["mobile"],
                    "course": s["course"],
                    "batch": s["batch"],
                }
            )
            status = "Created" if created else "Updated"
            self.stdout.write(f"  {status} Student : {student.student_id} - {student.name}")

            cert, c_created = Certificate.objects.update_or_create(
                certificate_id=s["cert_id"],
                defaults={
                    "student": student,
                    "title": "Internship Completion Certificate",
                    "issue_date": date(2025, 10, 15),
                    "course_name": s["course_name"],
                    "duration": s["duration"],
                    "grade": s["grade"],
                    "is_active": True,
                }
            )
            c_status = "Created" if c_created else "Updated"
            self.stdout.write(f"  {c_status} Certificate : {cert.certificate_id}\n")

        self.stdout.write(self.style.SUCCESS("Sample data loaded successfully!"))
        self.stdout.write(self.style.WARNING("\nTest with Student ID: 155049"))