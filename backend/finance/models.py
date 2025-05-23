from django.db import models

# Create your models here.

class Transaction(models.Model):
    # 1️⃣ Transaction types
    TRANSACTION_TYPE = [
        ('E', 'Expense'),
        ('I', 'Income'),
    ]

    # 2️⃣ Fixed category choices
    CATEGORY_CHOICES = [
    # Expense categories
    ('rent',           'Rent'),
    ('utilities',      'Utilities'),
    ('grocery',        'Grocery'),
    ('transport',      'Transport'),
    ('dining',         'Dining'),
    ('entertainment',  'Entertainment'),
    ('healthcare',     'Healthcare'),
    ('education',      'Education'),
    ('subscriptions',  'Subscriptions'),
    ('insurance',      'Insurance'),
    ('misc',           'Misc'),

    # Income categories
    ('salary',             'Salary'),
    ('bonus',              'Bonus'),
    ('gift',               'Gift'),
    ('dividends_interest', 'Dividends/Interest'),
    ('other',              'Other'),
]


    # 3️⃣ Fields
    date     = models.DateField(auto_now_add=True,db_index=True)
    type     = models.CharField(
                 max_length=1,
                 choices=TRANSACTION_TYPE,
                 help_text="‘E’ for Expense, ‘I’ for Income",
                 db_index=True
               )
    
    category = models.CharField(
                 max_length=20,
                 choices=CATEGORY_CHOICES,
                 help_text="Pick one of the predefined categories",
                 db_index=True
               )
    title    = models.CharField(max_length=255)
    amount   = models.DecimalField(max_digits=10, decimal_places=2)
    notes    = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']   # default sort: newest first

    def __str__(self):
        # Human-readable name in admin or shell
        return f"{self.get_type_display()} – {self.title} (${self.amount})"
