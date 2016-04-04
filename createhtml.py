import derekstudio
import random

def create_html_for_derek(data, date_data):

	print date_data
	print (len(date_data))
	d = {'suffix': data[0], 'parent_first': data[1], 'parent_last': data[2], 'email': data[3], 'instrument': data[4], 'student_name': data[5], 'student_age': data[6], 'additional_info': data[7]}
	print d
	if int(d['student_age']) < 8:
		video_selection = "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + derekstudio.rami.piano_pieces[0].yt_link +">" + "<img src=\"http://www.derekpiano.com/images/rami-polaroid.png\"></a></div>" + "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + derekstudio.zack.piano_pieces[0].yt_link +">" + "<img src=\"http://www.derekpiano.com/images/zack-polaroid.png\"></a></div>" + "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + derekstudio.meredith.piano_pieces[0].yt_link +">" + "<img src=\"http://www.derekpiano.com/images/meredith-polaroid.png\" alt=\"\"></a></div>" 
	elif int(d['student_age']) >= 8 and int(d['student_age']) <= 16:
		video_selection = "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + random.choice(derekstudio.travis.piano_pieces).yt_link +">" + "<img src=\"http://www.derekpiano.com/images/travis-polaroid.png\"></a></div>" + "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + random.choice(derekstudio.bennett.piano_pieces).yt_link +">" + "<img src=\"http://www.derekpiano.com/images/bennett-polaroid.png\"></a></div>" + "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + random.choice(derekstudio.ben.piano_pieces).yt_link +">" + "<img src=\"http://www.derekpiano.com/images/ben-polaroid.png\"></a></div>" 
	elif int(d['student_age']) >= 17:
		# Must be an adult
		video_selection = "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + random.choice(derekstudio.tap.piano_pieces).yt_link +">" + "<img src=\"http://www.derekpiano.com/images/tap-polaroid.png\"></a></div>" + "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + random.choice(derekstudio.daniel.piano_pieces).yt_link +">" + "<img src=\"http://www.derekpiano.com/images/daniel-polaroid.png\"></a></div>" + "<div style=\"width:200px; display:inline-block; vertical-align: top; padding-right: 40px; padding-top: 20px;\"><a href=" + random.choice(derekstudio.derek.piano_pieces).yt_link +">" + "<img src=\"http://www.derekpiano.com/images/derek-polaroid.png\"></a></div>" 
	else:
		video_selection = "Error"

	d['videomessage'] = video_selection



	if d['instrument'] == "None":
		instru = "Owning an instrument is a requirement for piano lessons and I will be glad to guide you in finding a suitable instrument for lessons. An acoustic piano is always preferred over a keyboard, but if your living situation does not allow a piano, there are suitable keyboards starting around $500. "
	elif d['instrument'] == "Has Keyboard":
		instru = "I noticed you already have a keyboard. It is essential your keyboard has 88 keys and basic weighted keys, keyboards that meet these specifications start around $500."
	else:
		instru = "I am so glad you already have a piano, we don't need to worry about purchasing an instrument!"

	d['instrument_message'] = instru

	meetfinal = ''
	for date, time in date_data:
		meetfinal += date + " at " + time + "<br>"

	if not meetfinal  == '':
		d['meeting'] = "<br><br>" + "I have the following times available to meet with you for our interview:<br> %s" % (meetfinal)
	else:
		d['meeting'] = ''

	if len(d['additional_info']) > 5:
		d['additional_info'] = '<br><br>' + d['additional_info']
	else:
		d['additional_info'] = ""

	html_msg = """<div style=\"background-color:#dadada\"><center><table
	id=\"Table_01\" width=\"800\" height=\"1739\" border=\"0\"
	cellpadding=\"0\" cellspacing=\"0\"> <tr> <td colspan=\"3\"> <a
	href=\"http://www.derekpiano.com\"><img
	src=\"http://www.derekpiano.com/images/email/derek_01.jpg\"
	width=\"800\" height=\"116\" alt=\"\"></td> </tr> <tr> <td
	colspan=\"3\"> <a href=\"http://www.derekpiano.com\"><img
	src=\"http://www.derekpiano.com/images/email/derek_02.jpg\"
	width=\"800\" height=\"449\" alt=\"\"></td> </tr> <tr> <td
	colspan=\"3\" bgcolor=\"f0f0f0\" height=200 style=\"padding: 20px;\">
	<font size=\"5\"><b>Dear {suffix} {parent_first} {parent_last},</b><br><font size=\"4\">My name is
	Derek Adam and I am a piano instructor at the Musical Arts Center of
	San Antonio. The placement team at MACSA informed me that you are
	currently looking for a piano instructor. I have earned two graduate
	piano degrees from UTSA and I am currently accepting more students
	into my piano studio. I would like to offer you a complimentary
	interview/mini-lesson so I can help {student_name} get
	started with piano lessons.{additional_info} {meeting} <br><br>Here are
	some links to a few of my students performing.<br> {videomessage} <br><br> {instrument_message} <br><br>Would you be available to
	meet at any of these times?<br><br>Thanks for considering piano
	lessons and I look forward to helping your family get started with
	piano lessons. </tr> <tr> <td colspan=\"3\"> <a
	href=\"http://www.derekpiano.com/#!About/c1wg9\"><img
	src=\"http://www.derekpiano.com/images/email/dereka_4.jpg\"
	width=\"800\" height=\"400\" alt=\"\"></td> </tr> <tr> <td
	colspan=\"3\"> <a
	href=\"https://www.youtube.com/watch?v=7Q90oE6Ng3g\"><img
	src=\"http://www.derekpiano.com/images/email/dereka_5.jpg\"
	width=\"800\" height=\"500\" alt=\"\"></td> </tr> <tr> <td> <a
	href=\"http://derekpiano.com\"><img
	src=\"http://www.derekpiano.com/images/email/derek_06.jpg\"
	width=\"319\" height=\"74\" alt=\"\"></td> <td> <img
	src=\"http://www.derekpiano.com/images/email/derek_07.jpg\"
	width=\"158\" height=\"74\" alt=\"\"></td> <td> <img
	src=\"http://www.derekpiano.com/images/email/derek_08.jpg\"
	width=\"323\" height=\"74\" alt=\"\"></td> </tr></table></center><!--
	End Save for Web Slices --></body>"""




	msg = html_msg.format(**d)

	with open('email_for_piano_prospective.html', 'w') as f:
		f.write(msg)