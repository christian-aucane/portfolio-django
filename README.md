# portfolio-django
A Django project for a portfolio

## TODO
- Mettre les ForeignKey de FontAwesomeIcon en PROTECT
- Ajouter des related_name a toutes les relations
- Ajouter les rendus HTML des icons dans l'interface admin (common.FontAwesomeIcon et awards.AwardCategory)
- Créer un dashboard pour remplir le site
- Ajouter des templatetags pour le rendu des elements
- Rassembler les apps des sections dans un dossier / tout rassembler dans une app ?
- Ajouter héritage de la classe MEta dans les models héritant de DisplayOrderBaseModel

## Management commands
Use `python manage.py <command>`

### populate_test_db
- Run migrations
- Populate the database with fake data
- Create a superuser
    - *Username :* admin
    - *Password :* admin
