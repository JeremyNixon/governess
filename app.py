from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'governesses-live-2026'

GOVERNESSES = [
    {
        'id': 1,
        'name': 'Sophia Chen',
        'year': 'Junior',
        'major': 'Linguistics & Classics',
        'languages': ['Mandarin', 'French', 'Latin', 'Ancient Greek'],
        'specialties': ['Classical Languages', 'Early Reading', 'Ancient Literature'],
        'bio': 'Raised between Shanghai and Paris, Sophia brings a rare cosmopolitan sensibility to early education. She believes in introducing children to classical texts in their original languages — Greek myths in Greek, Roman philosophy in Latin — fostering a relationship with ideas that no translation can fully replicate. Her youngest pupil began reading Ancient Greek at age seven.',
        'availability': 'Summer & Part-time',
        'rate': 'from $85 / hour',
        'location': 'San Francisco Bay Area',
        'quote': 'A child who reads Aesop in Greek will find all other texts waiting patiently for them.',
        'initials': 'SC',
    },
    {
        'id': 2,
        'name': 'Alexander Wright',
        'year': 'Senior',
        'major': 'Mathematics & Philosophy',
        'languages': ['English', 'German'],
        'specialties': ['Mathematics', 'Logic', 'Philosophy of Mind', 'History of Science'],
        'bio': 'Alexander spent a year at the University of Göttingen studying the history of mathematics before returning to Stanford. His approach mirrors that of Max Talmud — introducing children to Euclid and Spinoza not as curriculum to be completed, but as living intellectual adventures to be shared. He is particularly adept at kindling a love of mathematics in children who have been told they are "not math people."',
        'availability': 'Full-time',
        'rate': 'from $95 / hour',
        'location': 'New York · Remote Available',
        'quote': 'Geometry is not a school subject. It is the first encounter with eternal truth.',
        'initials': 'AW',
    },
    {
        'id': 3,
        'name': 'Isabella Marchetti',
        'year': 'Graduate Student',
        'major': 'Music & Italian Literature',
        'languages': ['Italian', 'French', 'Spanish', 'English'],
        'specialties': ['Piano', 'Composition', 'Renaissance Literature', 'Art History'],
        'bio': 'A concert pianist who studied at the Conservatorio di Milano before arriving at Stanford, Isabella weaves music theory, history, and literature into a unified curriculum. She treats Bach and Dante as contemporaries — both engaged in the same project of creating order from beauty. Two of her former pupils have performed at Carnegie Hall.',
        'availability': 'Weekends & Summer',
        'rate': 'from $110 / hour',
        'location': 'San Francisco Bay Area',
        'quote': 'Bach and Dante are speaking the same language. My task is to teach children to hear it.',
        'initials': 'IM',
    },
    {
        'id': 4,
        'name': 'James Park',
        'year': 'Senior',
        'major': 'Physics & Computer Science',
        'languages': ['Korean', 'English', 'Japanese'],
        'specialties': ['Physics', 'Mathematics', 'Programming', 'History of Science'],
        'bio': 'James approaches science education the way it was originally done — through biography and narrative. A child learning about electricity through the story of Faraday\'s life, or about gravity through Newton\'s obsessions, will understand something that no equation alone can convey. He has a particular talent for teaching physics to children as young as eight through the history of discovery.',
        'availability': 'Part-time · Remote',
        'rate': 'from $90 / hour',
        'location': 'Bay Area · Remote',
        'quote': 'Every equation is a chapter in a longer story. Begin with the story.',
        'initials': 'JP',
    },
    {
        'id': 5,
        'name': 'Catherine Beaumont',
        'year': 'Graduate Student',
        'major': 'History & Political Theory',
        'languages': ['French', 'English', 'Latin'],
        'specialties': ['History', 'Political Philosophy', 'Rhetoric', 'Essay Writing'],
        'bio': 'Catherine studied under a Rhodes Scholar at Oxford before arriving at Stanford. She specializes in what she calls "the education of the citizen" — teaching children not what to think, but how to argue, reason, and write with clarity and conviction. Her pupils routinely win national essay competitions, though that is, she insists, a side effect rather than a goal.',
        'availability': 'Full-time',
        'rate': 'from $100 / hour',
        'location': 'East Coast · Remote Available',
        'quote': 'The essay is not an assignment. It is the first act of intellectual courage.',
        'initials': 'CB',
    },
    {
        'id': 6,
        'name': 'Elena Volkov',
        'year': 'Junior',
        'major': 'Comparative Literature',
        'languages': ['Russian', 'German', 'French', 'English'],
        'specialties': ['Russian & European Literature', 'Languages', 'Early Reading', 'Poetry'],
        'bio': 'Born in St. Petersburg, Elena came to Stanford through the Hermitage programme. She has an unusual gift for teaching languages to very young children — through songs, stories, and poetry rather than grammar drills — and her reading programmes have produced children reading three years above their assessed level. She believes that the first language a child reads in shapes how they see the world.',
        'availability': 'Summer & Part-time',
        'rate': 'from $85 / hour',
        'location': 'Flexible',
        'quote': 'Teach a child to love reading in one language, and all others will follow as invitations.',
        'initials': 'EV',
    },
]


@app.route('/')
def index():
    return render_template('index.html', featured=GOVERNESSES[:3])


@app.route('/governesses')
def governesses():
    return render_template('governesses.html', governesses=GOVERNESSES)


@app.route('/governesses/<int:gid>')
def governess_detail(gid):
    governess = next((g for g in GOVERNESSES if g['id'] == gid), None)
    if not governess:
        return redirect(url_for('governesses'))
    return render_template('governess_detail.html', governess=governess)


@app.route('/families')
def families():
    return render_template('families.html')


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        flash('Your application has been received. We will be in touch within 48 hours.')
        return redirect(url_for('apply'))
    return render_template('apply.html')


@app.route('/inquire', methods=['GET', 'POST'])
def inquire():
    if request.method == 'POST':
        flash('Thank you for your inquiry. A member of our team will be in touch shortly.')
        return redirect(url_for('inquire'))
    return render_template('inquire.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
