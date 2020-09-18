# HTML გამოყენების საფუძვლები
HTML არის სტანდარტული მარკაპ ენა რომელიც გამოიყენება ვებ გვერდების შესქმნელად

## შესავალი [HTML Introduction](https://www.w3schools.com/html/html_intro.asp)
HTML ტიპის ფაილებს აქვთ `.html` გაფართოება. გაფართოება მიანიშნებს ტექსტურ ედიტორს
ან ვებ ბრაუზერს მიხვდეს თუ რა ტიპის ფაილთან აქვს ურთიერთობა. ახალი html
ფაილის შექმნისას ის უნდა შევინახოთ შესაბამის ფორმატში. 

მაგალითად:

`main.html`

ამ ფაილის გახსნისას ბრაუზერს ეცოდინება როგორ გამოიტანოს მასში მოთავსებული html კოდი.

## საწყისი შაბლონი
თანამედროვე ინტეგრირებული გარემოების (IDLE) უმრავლესობას, როგორიც არის PyCharm, WebStorm
Atom და ა.შ. აქვს ჩაშენებული საწყისი HTML-ის შაბლონი:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
```

### HTML ელემენტების ანატომია
![html თეგები](https://mdn.mozillademos.org/files/9347/grumpy-cat-small.png)

_[მსგავსება HTML-სა და Markdown ფორმატ შორის და ასევე უამრავი საჭირო თეგი თავისი მაგალითებით შეგიძლიათ ანხოთ ამ მისამართზე](https://www.markdownguide.org/basic-syntax/)_


HTML-ის ელემენტი მოთავსებულია შესაბამის tag-ებში. მაგ: `<title>Title</title>` 

მსგავსი ელემენტების თეგებს ვაერთიანებთ კომპონენტებში, კომპონენტის განმსაზღვრელ თეგებს შორის. მაგალითად
გვერდის ჰედერ ელემენტები მოთავსებულია `<head> </head>` თეგებს შორის.

head კომპონენტი ძირითადად ინახავს meta data-ს ვებ გვერზე, როგორიც არის CSS სტილთან კავშირი, ჯავასკრიპტთან კავშირი, 
ინფორმაცია ენკოდინგზე და ა.შ.

ძირითადი ფუნქციონალური HTML კოდი მოთავსდება `<body> </body>`

შესაბამისად საიტის ძირითადი კომპონენტები განისაზღვრება HTML ელემენტებით, ელემენტები
კი აღიწერება შესაბამისი თაგებით .html ფაილში.

## Div და Span 

Div და Span გვეხმარება html კოდის პორციებად სეგმენტირებაში. როდესაც დავიწყებთ ელემენტების
სტილის შექმნას CSS-ისა და Bootstrap-ის მეშვეობით, ხშირად გვექნება შემთხვევა როდესაც გარკვეული სტილის
გამოყენება მხოლოდ კონკრეტული ელემენტების სეგმენტზე გვჭირდება. ასეთ დროს გამოვიყენებთ div და span გამყოფებს.

### სინტაქსი:
```html
...
<div class="">
    <h1>სათაური</h1>
    <p>პარაგრაფი</p>
</div>
<p>პარაგრაფი div-ის გარეთ რომელიც <span>span თეგს შორის</span> მოვათავსეთ</p>

...
```

## ტექსტი, პარაგრაფი, ფორმატირება

### Heading | სათაურები 
```html
<h1>ძირითადი სათაური</h1>
<!-- etc -->
<h6>Level-6 სათაური</h6>
```

თეგი | ელემენტი
--- | ---
**h1** | მთავარი heading
**h6** | ნაკლებად მნიშვნელოვანი heading

### პარაგრაფები
```html
<p>პარაგრაფი.<br/>
ახალი ხაზი.</p>
<p>ახალი პარაგრაფი.</p>
<hr/>
<p>ნახეთ ხაზი ზემოთ.</p>
```

თეგი | ელემენტი
--- | ---
**p** | პარაგრაფი
**br** | ახალი ხაზი
**hr** | ჰორიზონტალური ხაზი

### ტექსტის ფორმატირება
```html
<em>Formatting</em> is <strong>important</strong> !
(a+b)<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup> + 2ab
```

თეგი | ელემენტი
--- | ---
**sub** | subscript
**sup** | superscript
**em** | emphasize
**strong** | important
**mark** | highlighted
**small** | small
**i** | italic
**b** | bold


## ატრიბუტები

ზოგ HTML ელემენტს გააჩნია ატრიბუტები, რომლითაც მათზე პირდაპირ შეიძლება მანიპულირება.
ატრიბუტების გამოყენებით შეგვიზლია ელემენტს დავუმატოთ ისეთი ნაწილი, როგორიცაა ვებ ბმული ან სურათის მისამართი.

### ბმულები
```html
<a href="url">ბმული</a>
<a href="url" target=_blank>გახსენი ბმული ახალ ფანჯარაში</a>

<a href="#comments">ბმული ელემენტზე id-ით კომენტარი</a>
<h2 id="comments">კომენტარი</h2>
```

თეგი | ელემენტი
--- | ---
**a** | hyperlink

<img src="https://www.flixist.com/wp-content/uploads/ul/226276-midnightgospel1.jpg" alt="description" width="300" height="200" />

### სურათები
```html
<img src="https://www.flixist.com/wp-content/uploads/ul/226276-midnightgospel1.jpg" alt="description" width="300" height="200" />
```
თეგი | ელემენტი
--- | ---
**img** | image

ატრიბუტი | აღწერა
--- | ---
src | მისამართი
alt | ტექსტი
width; height | სიგანე; სიმაღლე

## ფორმები

ვებ გვერდის ერთ-ერთი უმნიშვნელოვანეს ფუნქციონალია მომხმარებლისგან ინფორმაციის აღება. ინფორმაციის
ვებ გვერდის ინტერფეისიდან ამოღება ხდება html ფორმების გამოყენებით. იხილეთ html ფორმების მაგალითები: 

```html
<form action="url" method="post">
    <fieldset>
        <legend>რეგისტრაცია</legend>
        <label>Login :<input type="text" name="login" /></label><br/>
        <label for="pswd">Password :</label><input type="password" name="password" id="pswd" /><br/>
        <input type="radio" name="sex" value="male" />Male<br/>
        <input type="radio" name="sex" value="female" />Female<br/>
    </fieldset>
    
    <label>საყვარელი პოკემონი : <select name="color">
        <option>Charizard </option>
        <option>Gengar </option>
        <option>Greninja </option>
    </select></label>
    
    <input type="checkbox" name="available" value="monday" />ორშაბათი<br/>
    <input type="checkbox" name="available" value="tuesday" />სამშაბათი<br/>
    
    <textarea name="comments" rows="10" cols="30" placeholder="კომენტარის სივრცე"><textarea/>
    
    <input type="submit" value="ღილაკის ტექსტი">
</form>
```

თეგი | ელემენტი
--- | ---
**form** | form
**label** | label for input
**fieldset** | group inputs together
**legend** | legend for fieldset
**input** type="*text*" | text input
**input** type="*password*" | password input
**input** type="*radio*" | radio button
**input** type="*checkbox*" | checkbox
**input** type="*submit*" | send form
**select** | drop-down list
**option** | drop-down list item
**optgroup** | group of drop-down list items
**datalist** | autocompletion list
**textarea** | large text input

## ხშირად გამოყენებადი თეგები

### სია
```html
<ul>
    <li>item</li>
    <li>item</li>
    <li>item</li>
</ul>
```

თეგი | ელემენტი
--- | ---
**ul** | unordered list
**li** | list item

### მოწესრიგებული სია (დალაგებული)
```html
<ol>
    <li>first</li>
    <li>second</li>
    <li>third</li>
</ol>
```

თეგი | ელემენტი
--- | ---
**ol** | ordered list
**li** | list item

### სტანდარტული ცხრილი
```html
<table>
<tr>
    <th>სათაური 1</th>
    <th>სათაური 2</th>
</tr>
<tr>
    <td>მწკრივი 1, სვეტი 1</td>
    <td>მწკრივი 1, სვეტი 2</td>
</tr>
<tr>
    <td>მწკრივი 2, სვეტი 1</td>
    <td>მწკრივი 2, სვეტი 2</td>
</tr>
</table>
```

თეგი | ელემენტი
--- | ---
**table** | ცხრილი
**tr** | ცხრილის მწკრივი
**th** | ცხრილის დასახელება
**td** | ცხრილის უჯრა

## დამატებითი რესურსები
1. [HTML-ის სრული ვებ კურსი დეველოპერთათვის Mozilla-სგან](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [gendx | HTML Cheat Sheet](https://github.com/gendx/html-cheat-sheet#minimal-page)
