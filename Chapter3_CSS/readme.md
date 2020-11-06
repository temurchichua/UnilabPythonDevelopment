# CSS საფუძვლები
**Cascading Style Sheets**
CSS აღწერს თუ როგორ გამოჩნდება HTML ელემენტები ვებ გვერდზე.
CSS შეუძლია რამოდენიმე სხვადასხვა გვერდზე განლაგებულ ელემენტებზე იქონიოს გავლენა და ის როგორც
external [stylesheets](https://www.w3schools.com/css/css_intro.asp) ინახება CSS ფაილებში.

მაგ.: `style.css`

## სარჩევი
[TOC]



## css გამოყენება

CSS გვაძლევს შესაძლებლობას შევცვალოთ HTML ელემენტის სტილის ატრიბუტი/ები, როგორიცაა:
- ფერი
- ფონი
- ჩარჩო

CSS-თან მუშაობის პროცესი შეგვიძლია დავყოთ 4 ძირითად საფეხურად:
1. ვქმნით `.css` ფაილს
2. CSS სინტაქსის გამოყენებით ვაბამთ ელემენტის თეგებს
3. ვამატებთ სტილ ატრიბუტის property-value წყვილებს
4. ვაკავშირებთ CSS ფაილს HTML გვერდთან

## ტერმინოლოგია და ანატომია
![ანატომია](https://mdn.mozillademos.org/files/9461/css-declaration-small.png)

დასახელება | გამოყენება
--- | ---
Selector | ტეგის იდენტიფიკატორი
Property | პარამეტრი
Property Value | მნიშვნელობა
Declaration | გაწერა (სტილის)

### მაგალითი: 
```css
p {
  background-color: lightblue;
  color: white;
  text-align: center;
  font-family: verdana;
  font-size: 20px;
}
```

## HTML ფაილთან ბმა
ტეგი `<link>`-ის გამოყენებით ჩვენ შეგვიძლია HTML ფაილთნ მივაბათ სხვა ფაილები და 
შორის css stylesheet:

```html
  <head>

    <!-- Connect the html to the css file -->
    <link rel="stylesheet" href="style.css">

  </head>
```
ატრიბუტი `rel` აღნიშნავს ბმული ფაილის ტიპს/როლს _html_ ფაილისთვის, ხოლო
`href`-ში თავსდება იმ ფაილის მისამართი სადაც სტაილშიტია მოთავსებული.

## class და id
ყოველ HTML ელემენტს აქვს შესაძლებლობა მიენიჭოს class ან id ატრიბუტი. ეს თვისება
შესაძლებლობას გვაძლევს, რომ შევძლოთ კონკრეტული ელემენტის სტილის ცვლილება სტაილშიტიდან.

**class**-ის გამოყენებით შეგვიძლია გავაერთიანოთ სხვადასხვა (თუნდაც არაერთგვაროვანი ტიპის) html 
ელემენტი და მივანიჭოთ მათ საერთო მახასიათებელი.

**id**-ის მეშვეობით შეგვიძლია ინდივიდუალურად ავირჩიოთ html ელემენტი რომელზეც გვსურს რეაგირება.
შესაბამისად ყოველ ელემენტს უნდა ჰქონდეს უნიკალური ინდივიდუალური id მნიშვნელობა.

#### css სინტაქსი:
`#` - გამოიყენება id-ის გამოსაძახებლად
`.` - გამოიყენება class-ის გამოსაძახებლად

მაგალითად:
```css
.classname1{
    background: maroon;
}

#idname{
    background: green;
}
```

## სხვა ხშირად გამოყენებადი პარამეტრები
### ფონი
**ფონური ფერი**ს არჩევა:
```css
{
    background: gray;
}
```
ან ფერის არჩევა [ჰექს კოდით](https://www.color-hex.com/)
```css
{
    background: #AE78BE;
}
```

**ფონის სურათი**ს არჩევა მისამართიდან:
```css
{
    background: url(https://www.17thshard.com/forum/uploads/monthly_2018_10/Silmarillion_Tuor1.jpg.6200bf9c97e8100f9dddbbcddbd98f23.jpg);
}
```
პარამეტრი | მნიშვნელობა
--- | ---
background-repeat | no-repeat

### ჩარჩო


```css
div{
    background: maroon;
    border: orange;
    border-width: thick;
    border-style: dotted;
}
```
ან
```css
div{
    background: maroon;
    border: royalblue 2px dashed;
}
```

### ფონტი
#### ჩაშენებული ფონტების გამოყენება
```css
p {
  font-family: verdana;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}
```
#### ვებ-ფონტების გამოყენება
