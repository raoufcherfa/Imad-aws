# API pour la présentation des employés

Cette API permet de communiquer avec un front-end développé en Angular pour afficher les employés avec les informations suivantes :

Employé :
- id : entier
- firstName: string
- lastName: string
- emailId: string

L'API sera accessible à l'adresse suivante : `http://localhost:8081/api/v1`

## Endpoints

Les endpoints disponibles sont les suivants :

### GET /employees
Cet endpoint permet de récupérer la liste de tous les employés.

### POST /employees
Cet endpoint permet de créer un nouvel employé en envoyant les données nécessaires dans le corps de la requête.

### DELETE /employees/id
Cet endpoint permet de supprimer un employé en spécifiant son `id`.

### PUT /employees/id
Cet endpoint permet de mettre à jour les informations d'un employé en spécifiant son `id` et en envoyant les nouvelles données dans le corps de la requête.
