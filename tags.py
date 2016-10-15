def tags(publisher):
	if (publisher == "All Recipes"):
		tag = '//span[@class="recipe-directions__list--item"]/text()'
	elif (publisher == "Back to Her Roots"):
		tag = '//li[@class="instruction"]/text()'
	elif (publisher == "BBC Food"):
		tag = '//p[@class="recipe-method__list-item-text"]/text()'
	else :
		return 404
	return tag
