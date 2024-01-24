class ContactForm {
    // Constructor
    constructor(url) {
        this.url = url;
        this.setUpEventListeners();
    }

    
    // VALIDATION FUNCTIONS
    
    // Function to validate an email address
    isValidEmail(email) {
        // Use a regular expression to validate the email address
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    };

    // Function to check that all fields are valid
    checkFormValidity() {
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('emailAddress').value.trim();
        const subject = document.getElementById('subject').value.trim();
        const message = document.getElementById('message').value.trim();
        const consent = document.getElementById('consentCheckbox').checked;
        const submitButton = document.getElementById('submitButton');
    
        // Activates the submit button if all fields are valid, otherwise deactivates it.
        if (name !== '' && this.isValidEmail(email) && subject !== '' && message !== '' && consent) {
            submitButton.removeAttribute('disabled');
        } else {
            submitButton.setAttribute('disabled', 'disabled');
        };
    };

    // Function to validate the field when it loses focus
    validateField(fieldId) {
        const field = document.getElementById(fieldId);
        const fieldValue = field.value.trim();
        const errorContainer = document.getElementById(`${fieldId}Error`);
        
        // Checks if the field is empty
        if (fieldValue === '') {
            errorContainer.textContent = 'Ce champ est requis.';
        } else {
            // Checks email address if field is email
            if (fieldId === 'emailAddress') {
                if (!this.isValidEmail(fieldValue)) {
                    errorContainer.textContent = 'Adresse email non valide.';
                    return;
                };
            };
    
            // Clears error message if any
            errorContainer.textContent = '';
        }
    
        // Checks if all fields are valid to activate the submit button
        this.checkFormValidity();
    };

    // Function to validate the consent checkbox
    validateConsentCheckbox() {
        const consentCheckbox = document.getElementById('consentCheckbox');
        const consentCheckboxError = document.getElementById('consentCheckboxError');
    
        // Checks if the checkbox is ticked
        if (!consentCheckbox.checked) {
            consentCheckboxError.textContent = 'Vous devez consentir à l\'utilisation de votre adresse e-mail.';
        } else {
            consentCheckboxError.textContent = '';
        };
    
        // Checks if all fields are valid to activate the submit button
        this.checkFormValidity();
    };

    
    // SUBMISSION

    // Function to manage form submission
    submitForm() {
        const form = document.getElementById('contactForm');
        const submitButton = document.getElementById('submitButton');
        const successMessage = document.getElementById('submitSuccessMessage');
        const errorMessage = document.getElementById('submitErrorMessage');
    
        // Disables the submit button and displays the loader
        submitButton.setAttribute('disabled', 'disabled');
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Envoi en cours...';
    
        // Retrieves form data
        const formData = new FormData(form);
        console.log(formData);
        // Envoie la requête AJAX
        fetch(this.url, {
            method: "POST",
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // La requête a réussi, masque le bouton et affiche le message de succès
                submitButton.classList.add('d-none');
                successMessage.classList.remove('d-none');
                errorMessage.classList.add('d-none');
            } else {
                // La requête a échoué, affiche le message d'erreur et réactive le bouton
                errorMessage.classList.remove('d-none');
                submitButton.removeAttribute('disabled');
                submitButton.innerHTML = 'Envoyer';
            };
        })
        .catch(error => {
            // Gère les erreurs réseau, affiche le message d'erreur et réactive le bouton
            errorMessage.classList.remove('d-none');
            submitButton.removeAttribute('disabled');
            submitButton.innerHTML = 'Envoyer';
        });
    };


    // EVENT LISTENERS

    // Function to set up event listeners
    setUpEventListeners() {
        // Add event listener for form submission
        document.getElementById('contactForm').addEventListener('submit', (event) => {
            event.preventDefault();
            this.submitForm();
        });
    
        // Add event listeners for each field
        document.getElementById('name').addEventListener('blur', () => {
            this.validateField('name');
        });
        document.getElementById('emailAddress').addEventListener('blur', () => {
            this.validateField('emailAddress');
        });
        document.getElementById('subject').addEventListener('blur', () => {
            this.validateField('subject');
        });
        document.getElementById('message').addEventListener('blur', () => {
            this.validateField('message');
        });
    
        // Add event listener for the consent checkbox
        document.getElementById('consentCheckbox').addEventListener('change', () => {
            this.validateConsentCheckbox();
        });
    };
}