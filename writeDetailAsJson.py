# coding: utf-8
import json

details_english = {
	"title": "Fei Liang",
	"navbar": {
		'brand': 'Fei Liang',
		'navitem': ['Home', 'Skills', 'About Me', 'Contact', 'Resume'],
		'link': '中文'
		},
	"self_introduction": {
		"interests": 'Software Engineer &amp; Machine Learning'
		},
	"interests": {
		'head': 'What I have learned (and done)',
		'contents': [
			{'title': 'Machine Learning. ', 
			 'intro': 'Machine Learning &amp; Data Mining &amp; Deep Learning',
			 'projects': [
			 	'Image Classification of Dogs and Cats using Gaussian Process',
			 	'Clustering and Classification for Gene Functions'
			]},
			{'title': 'Big Data and Cloud Computing.', 
			 'intro': 'MapReduce &amp; Spark',
			 'projects': [
			 	'Spam Detection Filter',
			 	'Recommendation System Based on Netflix Rating Dataset'
			]},
			{'title': 'Full Stack Web Development. ', 
			 'intro': 'Django &amp; HTML &amp; CSS &amp; jQuery',
			 'projects': [
			 	'Star Social: Website Development'
			]},
			{'title': 'Software Development. ', 
			 'intro': 'iOS Applications &amp; Video Games',
			 'projects': [
			 	'Rate Y: iOS Application Development',
			 	'Scarlet Devil: 3D Video Game Development'
			]}
		],
		'tail': 'For more details, please check my resume'
	},
	"skills": [
		{
			'general': 'Machine Learning',
			'general_score': '90',
			'list': [
			 	{'name': 'Python',
			 	 'score': '90'},
			 	{'name': 'R',
			 	 'score': '50'},
			 	{'name': 'MATLAB',
			 	 'score': '60'},
			 	{'name': 'Spark',
			 	 'score': '70'}
			]
		},
		{
			'general': 'MapReduce &amp; Spark',
			'general_score': '80',
			'list': [
			 	{'name': 'MapReduce',
			 	 'score': '50'},
			 	{'name': 'Hadoop Streaming &amp; Python',
			 	 'score': '90'},
			 	{'name': 'PySpark',
			 	 'score': '70'}
			]
		},
		{
			'general': 'Full Stack Web Development',
			'general_score': '65',
			'list': [
			 	{'name': 'HTML',
			 	 'score': '80'},
			 	{'name': 'CSS',
			 	 'score': '70'},
			 	{'name': 'JavaScript/jQuery',
			 	 'score': '60'},
			 	{'name': 'Django',
			 	 'score': '50'}
			]
		},
		{
			'general': 'Software Development',
			'general_score': '70',
			'list': [
			 	{'name': 'Swift',
			 	 'score': '80'},
			 	{'name': 'Unity',
			 	 'score': '65'}
			]
		}
	],
	"about_me" : {
		'title': 'About Me ... ',
		'school': 'I graduated from Washington University in St. Louis this year (2017)',
		'major': 'My major is Computer Science, and I got the certificate in Machine Learning and Data Mining',
		'freetime': 'In my free time I play table tennis and try some new techniques',
		'learning': 'Currently I am learning more about Spark and iOS',
		'other': 'Life is short, I love Python'
	},
	"links": {
		'title': 'Links'
	}
}



print('start to write to details')
with open('details', 'wb', ) as f:
	detail_json = json.dumps(details_english, ensure_ascii=False).encode('utf-8')
	f.write(detail_json)
print('successfully write to details')
