# portfolio-django
A Django project for a portfolio

## Liens utiles
- [Boite de dialogue](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)

## TODO
- Mettre les ForeignKey de FontAwesomeIcon en PROTECT
- Ajouter des related_name a toutes les relations
- Ajouter les rendus HTML des icons dans l'interface admin (common.FontAwesomeIcon et awards.AwardCategory)
- Créer un dashboard pour remplir le site
- Ajouter des templatetags pour le rendu des elements
- Rassembler les apps des sections dans un dossier / tout rassembler dans une app ?
- Ajouter héritage de la classe Meta dans les models héritant de DisplayOrderBaseModel
- Ajuster le centrage des images dans les card
- Ajouter analytique sur les liens (compteur et redirection)
- Faire du code lint dans tous les fichiers (utiliser une librairie pour ca)
- Ajouter traduction dans les templates d'email et dans le template index (formulaire)
- Créer vues qui affiche les threads (dashboard et user) et permet de répondre directement dans la vue

## PROCHAINE ETAPE
- Faire un pull sur le main
- Faire le dashboard
  - remplir toutes les sections a partir du dashboard
  - ajouter contacts
  - ajouter analytics

## Management commands
Use `python manage.py <command>`

### populate_test_db
- Make migrations
- Run migrations
- Populate the database with fake data
- Create a superuser
    - **Username :** admin
    - **Password :** admin
