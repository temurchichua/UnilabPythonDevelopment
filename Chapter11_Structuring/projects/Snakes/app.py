from project import app, db
from flask import render_template
from project.models import Snakes



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':

    data = [('Xerotyphlops vermicularis', 'გველბრუცა', 'X_vermicularis.jpg'),
            ('Eryx jaculus', 'დასავლეთის მახრჩობელა', 'E_jaculus.jpg'),
            ('Coronella austriaca', 'სპილენძა',  'C_austriaca.jpg'),
            ('Dolichophis schmidti', 'წითელმუცელა მცურავი', 'D_schmidti.jpg'),
            ('Eirenis collaris', 'საყელოიანი ეირენისი', 'E_collaris.jpg'),
            ('Eirenis modestus', 'წყნარი ეირენისი', 'E_modestus.jpg'),
            ('Elaphe dione', 'სახეებიანი მცურავი', 'E_dione.jpg'),
            ('Elaphe urartica', 'ურარტუს ოთხზოლიანი მცურავი', 'E_urartica.jpg'),
            ('Hemorrhois ravergieri', 'ნაირფერი მცურავი', 'H_ravergieri.jpg'),
            ('Molpolon insignitus', ' აღმოსავლური ხვლიკიჭამია გველი', 'M_insignitus.jpg'),
            ('Natrix natrix', 'ჩვეულებრივი ანკარა', 'N_natrix.jpg'),
            ('Natrix tessellata', 'წყლის ანკარა', 'N_tessellata.jpg'),
            ('Platyceps najadum', 'წენგოსფეწრი მცურავი', 'P_najadum.jpg'),
            ('Telescopus fallax', 'კატისთვალა გველი', 'T_fallax_1.jpg'),
            ('Zamenis hohenackeri', 'ამიერკავკასიური მცურავი', 'Z_hohenackeri.jpg'),
            ('Zamenis longissimus', 'ესკულაპის მცურავი', 'Z_longissimus.jpg'),
            ('Macrovipera lebetina', 'გიურზა', 'M_lebetina_1.jpg'),
            ('Vipera transcaucasiana', 'ამიერკავკასიური ცხვირრქოსანი გველგესლა', 'V_transcaucasiana.jpg'),
            ('Vipera darevskii', 'დარევსკის გველგესლა', 'V_darevski.jpg'),
            ('Vipera dinniki', 'დინიკის გველგესლა', 'V_dinniki.jpg'),
            ('Vipera eriwanensis', 'სომხური ველის გველგესლა', 'V_eriwanensis.jpg'),
            ('Vipera kaznakovi', 'კავკასიური გველგესლა', 'V_kaznakovi.jpg')
            ]

    if Snakes.query.first():
        pass
    else:
        for item in data:
                snake = Snakes(item[0], item[1], item[2])
                db.session.add(snake)

        db.session.commit()

    app.run(debug=True, port=8000)
