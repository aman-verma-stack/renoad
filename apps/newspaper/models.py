from django.db import models

# Create your models here.

class Newspaper(models.Model):
    newspaper = models.CharField(max_length=150, null=True, blank=True)
    newspaper_image = models.ImageField(upload_to='newspaper',null=True, blank=True)

    def __str__(self):
        return self.newspaper

    class Meta:
        managed = True
        verbose_name = 'Newspaper'
        verbose_name_plural = 'Newspapers'



def move_data():
    data = ["AAJ","Ajit","AJit Samachar","Amar Ujala","Anand Bazar Patrika","Andhra Jyothi","Andhra Prabha","Asomiya Pratidin","Assam Tribune","Assignment Abroad Times","Bartman","Business by bids - ET","Business by bids - NBT","Business by bids - TOI","Daily Excelsior","Daily Hindi Milap","Daily Thanthi","Dainik Bhaskar","Dainik Jagran","Dainik Navajyoti","Dainik Savera Times","Dainik Tribune","Deccan Chronicle","Deccan Herald","Deshbandhu","Dharitri","Dinakaran","Dinamalar","Divya Bhaskar","DNA","Education Times","Eenadu","Ei Samay","EkDin","Greater Kashmir","Gujarat Samachar","Gujarati mid day","Hind Samachar","Hindustan Hindi","Hindustan Times","Hindustan Times Classified Special","HT Education","HT Mint","INEXT","Inquilab","Jagbani","Kannada Prabha","Lokmat","Loksatta","Maharashtra Times","Malayala Manorama","Mathrubhumi","mid day","Mirror","Mumbai Choufer","Munsif daily","Nai Dunia","Nav Gujrat Samay","Navabharat","Navbharat Times","Navodaya Times","Navshakti","Prabhat Khabar","Prajavani","Property Times","Pudhari","Punjab Kesari(Delhi Group)","Punjab Kesari(Jalandhar Group)","Punjabi Tribune","Punya Nagari","Raj Express","Rajasthan Patrika","Rashtradoot","Rashtriya Hindi Mail","Rashtriya Sahara","Saamna","Sakal","Sakshi","Samachar jagat","Sambad","Samyukta Karnataka","Sandesh","Sandhya Times","Sandhyanand","Star of Mysore","The Arunachal Times","The Economic Times","The Free Press Journal","The Hindu","The Indian Express","The Navhind Times","The Pioneer","The pioneer hindi","The Siasat Daily","The Telegraph","The Times of India","The Tribune","Times Zigwheels","Udayavani","Vijay Karnataka","Vijayavani","Vir Arjun","Yashobhumi"]

    for e in data:
        print(e)
        # new = Newspaper(
        #     newspaper = e
        # )
        # new.save()