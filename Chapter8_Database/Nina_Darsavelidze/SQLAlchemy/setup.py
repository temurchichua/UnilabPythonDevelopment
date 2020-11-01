from basic import db, GalleryGiftShop

db.create_all()

item1 = GalleryGiftShop(20297, 'სარკე', 'გიორგი გელაძე', 'ნამუშევრის ზომა არის 90x30 და წარმოდგენილია გიორგი გელაძის გამოფენიდან "ღიმილი მოდის გულიდან🕉"', 600)
item2 = GalleryGiftShop(20297, 'ფაზლი', 'სალომე დუმბაძე', 'ნამუშევრის ზომა არის 20x30 და არის დაბეჭდილი სალომე დუმბაძის ნამუშევრის მიხედვით', 50)

db.session.add_all(item1, item2)

db.session.commit()

print(item1.id)

print(item2.id)
