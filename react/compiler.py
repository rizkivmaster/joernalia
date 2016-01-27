def compile(filenames, target):
	alljsx=''
	for filename in filenames:
		lines=open(filename, 'r').readlines()
		for line in lines:
			alljsx+=line
	from react import jsx
	transformer = jsx.JSXTransformer()
	js = transformer.transform_string(alljsx)
	open(target, 'w').write(js)
	print('all written')