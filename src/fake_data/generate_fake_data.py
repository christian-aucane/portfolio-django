import random

from faker import Faker
from django.core.files import File
from django.contrib.auth import get_user_model
from django.utils.translation import gettext

from about.models import AboutInfo, AboutSkill, SocialLink
from awards.models import AwardCategory, Award
from common.models import FontAwesomeIcon
from contact.models import ContactMessage, ContactThread
from education.models import Education
from experience.models import Experience
from interests.models import Paragraph
from projects.models import Technology, Category, Project, ProjectCategory, ProjectTechnology, ProjectLink
from skills.models import Skill


User = get_user_model()

fake = Faker()

# TODO : gérer les dates de debut et de fin correctement (date de fin >= date de debut) et pour chaque experience une
#  date de début qui est apres la date de fin de l'experience précédente

# TODO : Ajouter docstrings

THUMBNAIL = File(open("fake_data/fake_thumbnail.jpg", 'rb'))

FILE = File(open("fake_data/fake_file.pdf", 'rb'))

USED_WORDS = []


def get_unique_fake_word(nb=1):
    words = []
    for _ in range(nb):
        word = fake.word()
        while word in USED_WORDS:
            word = fake.word()
        USED_WORDS.append(word)
        words.append(word)
    return " ".join(words)


# ABOUT

def generate_about_info():
    about_info = AboutInfo.objects.first()
    about_info.first_name = fake.first_name()
    about_info.last_name = fake.last_name()
    about_info.description = fake.text(max_nb_chars=600)
    about_info.profile_thumbnail = THUMBNAIL
    about_info.save()


def generate_about_skills():
    about_skills = [AboutSkill(name=get_unique_fake_word()) for _ in range(5)]
    AboutSkill.objects.bulk_create(about_skills)


def generate_social_links():
    fb_icon, _ = FontAwesomeIcon.objects.get_or_create(title="facebook", css_classes="fab fa-facebook")
    instagram_icon, _ = FontAwesomeIcon.objects.get_or_create(title="instagram", css_classes="fab fa-instagram")
    linkedin_icon, _ = FontAwesomeIcon.objects.get_or_create(title="linkedin", css_classes="fab fa-linkedin")

    social_links = [
        SocialLink(name="Facebook", url="https://facebook.com", icon=fb_icon),
        SocialLink(name="Instagram", url="https://instagram.com", icon=instagram_icon),
        SocialLink(name="LinkedIn", url="https://linkedin.com", icon=linkedin_icon),
    ]
    SocialLink.objects.bulk_create(social_links)


# EXPERIENCE

def generate_experiences():
    experiences = [
        Experience(
            title=fake.job(),
            company=fake.company(),
            description=fake.text(),
            thumbnail=THUMBNAIL,
            start_date=fake.date(),
            end_date=fake.date()
        ) for _ in range(5)]
    Experience.objects.bulk_create(experiences)


# EDUCATION

def generate_educations():
    educations = [
        Education(
            school_name=fake.company(),
            program=get_unique_fake_word(),
            role=fake.job(),
            description=fake.text(max_nb_chars=50),
            start_date=fake.date(),
            end_date=fake.date(),
            thumbnail=THUMBNAIL
        ) for _ in range(5)
    ]
    Education.objects.bulk_create(educations)


# SKILLS

def generate_skills():
    languages_icons = [
        FontAwesomeIcon.objects.get_or_create(title="python", css_classes="fab fa-python")[0],
        FontAwesomeIcon.objects.get_or_create(title="java", css_classes="fab fa-java")[0],
        FontAwesomeIcon.objects.get_or_create(title="javascript", css_classes="fab fa-js")[0],
        FontAwesomeIcon.objects.get_or_create(title="php", css_classes="fab fa-php")[0],
        FontAwesomeIcon.objects.get_or_create(title="html", css_classes="fab fa-html5")[0],
    ]
    languages = [
        Skill(
            name=icon.title,
            category="language",
            icon=icon,
        ) for icon in languages_icons
    ]
    Skill.objects.bulk_create(languages)

    frameworks_icons = [
        FontAwesomeIcon.objects.get_or_create(title="Python", css_classes="fab fa-python")[0],
        FontAwesomeIcon.objects.get_or_create(title="HTML", css_classes="fab fa-html5")[0],
        FontAwesomeIcon.objects.get_or_create(title="CSS", css_classes="fab fa-css3-alt")[0],
    ]
    frameworks = [
        Skill(
            name=fake.word(),
            category="framework",
            icon=fake.random_element(frameworks_icons),
        ) for _ in range(8)
    ]
    Skill.objects.bulk_create(frameworks)

    workflow_icon, _ = FontAwesomeIcon.objects.get_or_create(title="Check", css_classes="fas fa-check")
    workflows = [
        Skill(
            name=get_unique_fake_word(),
            category="workflow",
            icon=workflow_icon
        ) for _ in range(5)
    ]
    Skill.objects.bulk_create(workflows)


# PROJECTS
def generate_projects():
    technologies_icons = [
        FontAwesomeIcon.objects.get_or_create(title="Python", css_classes="fab fa-python")[0],
        FontAwesomeIcon.objects.get_or_create(title="HTML", css_classes="fab fa-html5")[0],
        FontAwesomeIcon.objects.get_or_create(title="CSS", css_classes="fab fa-css3-alt")[0],
    ]

    technologies = []
    for _ in range(20):
        technologies.append(
            Technology.objects.create(
                name=get_unique_fake_word(),
                icon=fake.random_element(technologies_icons)
            )
        )

    categories = []
    for _ in range(8):
        categories.append(
            Category.objects.create(name=get_unique_fake_word())
        )

    links_data = [
        {
            "title": "Github",
            "link": "https://github.com",
            "icon": FontAwesomeIcon.objects.get_or_create(title="Github", css_classes="fab fa-github")[0],
            "text": gettext("See the code")
        },
        {
            "title": "Website",
            "link": "https://example.com",
            "icon": FontAwesomeIcon.objects.get_or_create(title="Globe", css_classes="fas fa-globe")[0],
            "text": gettext("See the website")
        },
        {
            "title": "Specifications",
            "link": "https://example.com",
            "icon": FontAwesomeIcon.objects.get_or_create(title="List", css_classes="fas fa-list")[0],
            "text": gettext("See the specifications")
        }
    ]

    for _ in range(5):
        project = Project.objects.create(
            name=get_unique_fake_word(random.randint(3, 8)),
            description=fake.text(),
            thumbnail=THUMBNAIL
        )

        project_categories = random.sample(categories, k=random.randint(1, 3))
        for category in project_categories:
            project_category = ProjectCategory.objects.create(
                project=project,
                category=category
            )

            project_technologies = random.sample(technologies, k=random.randint(2, 5))
            for technology in project_technologies:
                ProjectTechnology.objects.create(
                    project_category=project_category,
                    technology=technology
                )

        project_links_data = random.sample(links_data, k=2)
        project_links = [ProjectLink(project=project, **link_data) for link_data in project_links_data]
        ProjectLink.objects.bulk_create(project_links)


# INTERESTS

def generate_interests():
    paragraphs = [
        Paragraph(
            title=get_unique_fake_word(),
            text=fake.text(max_nb_chars=400),
        ) for _ in range(3)
    ]
    Paragraph.objects.bulk_create(paragraphs)


# AWARDS

def generate_awards():
    def generate(category):
        obtained = random.randint(0, 3) >= 1
        return Award(
            title=get_unique_fake_word(random.randint(3, 8)),
            text=fake.text(max_nb_chars=random.randint(25, 80)),
            category=category,
            file=FILE if obtained else None,
            obtain_date=fake.date() if obtained else None
        )
    trophy_icon, _ = FontAwesomeIcon.objects.get_or_create(
        title="trophy", css_classes="fas fa-trophy"
    )
    trophy_category, _ = AwardCategory.objects.get_or_create(
        title="Trophies", icon=trophy_icon, icon_color="text-warning"
    )
    trophies = [generate(trophy_category) for _ in range(random.randint(3, 10))]
    Award.objects.bulk_create(trophies)

    courses_icon, _ = FontAwesomeIcon.objects.get_or_create(
        title="book", css_classes="fas fa-book"
    )
    courses_category, _ = AwardCategory.objects.get_or_create(
        title="Courses", icon=courses_icon, icon_color="text-success"
    )

    courses = [generate(courses_category) for _ in range(random.randint(3, 10))]
    Award.objects.bulk_create(courses)


def generate_contact_messages():
    for _ in range(5):
        ContactMessage.new_contact(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            subject=get_unique_fake_word(random.randint(3, 8)),
            message=fake.text(),
            gdpr_consent=True
        )
    for thread in ContactThread.objects.all():
        for _ in range(random.randint(1, 5)):
            ContactMessage.add_message_to_thread(
                thread_uuid=thread.uuid,
                email=fake.email,
                message=fake.text()
            )


def generate_fake_data():

    generate_about_info()
    generate_about_skills()
    generate_social_links()
    generate_experiences()
    generate_educations()
    generate_skills()
    generate_projects()
    generate_interests()
    generate_awards()

    generate_contact_messages()

    THUMBNAIL.close()
    FILE.close()


if __name__ == "__main__":
    generate_fake_data()
