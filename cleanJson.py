import json

def writeToJSONFile(fileName, data):
    filePathNameExt = './'+'Json/'+ fileName + '.json'
    try:
        with open(filePathNameExt, 'a+') as fp:
            json.dump(data, fp)
    except Exception as ex:
        print(ex)
    finally:
        fp.close()
def clean(file):
    parser = json.JSONDecoder()
    parsed = []
    with open(file) as f:
        data = f.read()
    head = 0
    while True:
        head = (data.find('{', head) + 1 or data.find('[', head) + 1) - 1
        try:
            struct, head = parser.raw_decode(data, head)
            parsed.append(struct)
        except (ValueError, json.JSONDecodeError):
            break

    file2="./Json/output.json"
    with open(file2,'a+') as f:
        json.dump(parsed, f, indent=2)
clean("./Json/articles_raw.json")
articleList = []
ArticleFile = "Article"
article_id = 1;

with open("./Json/output.json", "r") as in_file:
    data = json.load(in_file)
    for x in data:
        temp = {}

        temp['article_id'] = article_id;
        if 'title' in x:
            if 'ftext' in x['title']:
                article_name = x['title']['ftext'].replace(',', '')
                if not article_name:
                    continue
                temp['article_name'] = article_name
            else:
                continue
        else:
            continue

        if 'pages' in x:
            if 'ftext' in x['pages']:
                pg_no = x['pages']['ftext']
                if not pg_no:
                    continue
                temp['pg_no'] = pg_no
            else:
                continue
        else:
            continue

        if 'year' in x:
            if 'ftext' in x['year']:
                year_published = x['year']['ftext']
                if not year_published:
                    continue
                temp['year_published'] = year_published
            else:
                continue
        else:
            continue

        if 'volume' in x:
            if 'ftext' in x['volume']:
                volume_id = x['volume']['ftext']
                if not volume_id:
                    continue
                temp['volume_id'] = volume_id
            else:
                continue
        else:
            continue

        if 'journal' in x:
            if 'ftext' in x['journal']:
                magazine_name = x['journal']['ftext'].replace(',', ' ')
                if not magazine_name:
                    continue
                temp['magazine_name'] = magazine_name
            else:
                continue
        else:
            continue

        if 'author' in x:
            author = x['author']
            if(type(author) == list):
                for y in author:
                    temp_copy = temp.copy()
                    author_temp = y['ftext']
                    author_name_list = author_temp.split()
                    temp_copy['fname'] = author_name_list[0]
                    temp_copy['lname'] = author_name_list[-1]
                    articleList.append(temp_copy)
            else:
                if not author:
                    continue
                author_name_list= author['ftext'].split()
                temp['fname'] = author_name_list[0]
                temp['lname'] = author_name_list[-1]
                articleList.append(temp)
        else:
            continue

        article_id = article_id + 1

writeToJSONFile(ArticleFile, articleList)
