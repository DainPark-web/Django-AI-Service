from django.db import models
import hashlib
import secrets

# Create your models here.
class AiKey(models.Model):
    key_hash = models.CharField(max_length=64, blank=True, null=True)  # For SHA-256 hash
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)    

    def __str__(self):
        return f"API Key for {self.user.username}"

    @staticmethod
    def generate_key():
        """Generate a random API key"""
        return secrets.token_urlsafe(32)

    @staticmethod
    def hash_key(key):
        """Hash the API key"""
        return hashlib.sha256(key.encode()).hexdigest()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only when creating new key
            # Generate the actual key
            raw_key = self.generate_key()
            # Store the hash
            self.key_hash = self.hash_key(raw_key)
            # Save the model
            super().save(*args, **kwargs)
            # Attach the raw key temporarily so it can be shown once
            self.raw_key = raw_key
            print(f"Generated key: {raw_key}")
        else:
            super().save(*args, **kwargs)

    def verify_key(self, key_to_verify):
        """Verify if a given key matches the stored hash"""
        return self.key_hash == self.hash_key(key_to_verify) 