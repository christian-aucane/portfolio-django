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
- Ajuster le centrage des images dans les card
- Ajouter analytique sur les liens (compteur et redirection)
- Faire du code lint dans tous les fichiers (utiliser une librairie pour ca)
- Ajouter les tests des models manquants

## Management commands
Use `python manage.py <command>`

### populate_test_db
- Make migrations
- Run migrations
- Populate the database with fake data
- Create a superuser
    - **Username :** admin
    - **Password :** admin
