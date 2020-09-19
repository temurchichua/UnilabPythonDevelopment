# Bootstrap4 - Front End მეგობარი
### [შესავალი](https://getbootstrap.com/docs/4.5/getting-started/introduction/) | [მაგალითები](https://getbootstrap.com/docs/4.5/examples/) | [დოკუმენტაცია](https://getbootstrap.com/docs/4.5/layout/overview/)
Boostrap არის მსოფლიოში ერთ-ერთი ყველაზე პოპულარული ფრონტ-ენდ დეველოპმენტ იარაღების ნაკრები, 
რომელიც დაგეხმარება სწრაფად და მარტივად მოათავსო წინასწარ გამზადებული კომპონენტები შენს გვერდზე,
ფრონტ ენდის ასაწყობად.

## სარჩევი
- [გამოყენება](#როგორ-გამოვიყენოთ-bootstrap)
- [კომპონენტები](#კომპონენტები)
- [კონტეინერი](#კონტეინერი)
- [ღილაკები](#ღილაკები)



## როგორ გამოვიყენოთ Bootstrap

არსებობს Bootstrap-ის პროექტში ჩაშენების რამოდენიმე გზა. თქვენ შეგიძლიათ ინდივიდუალურად [გადმოწეროთ Bootstrat](https://getbootstrap.com/docs/4.5/getting-started/download/)
სორს კოდთან და კომპონენტებთან ერთად [ვებ გვერდიდან](https://getbootstrap.com/docs/4.5/getting-started/download/) ან რომელიმე
სასურველი Package Manager-ის მეშვეობით (npm, yarn, RubyGems, NuGet, Composer), ან შემოიტანოთ შესაბამისი ბმულები html ფაილში,
[BootstrapCDN](https://www.bootstrapcdn.com/) ის მეშვეობით.
```html
<!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<!-- JS, Popper.js, and jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script> 
```
ფაილის header-ში შესაბამისი ბმულების დამატებით შეძლებთ გვერდზე [Bootstrap კომპონენტების](https://getbootstrap.com/docs/4.5/components/) პირდაპირ ჩაშენებას.

## [კომპონენტები](https://getbootstrap.com/docs/4.5/components/)

**კომპონენტი** Bootstrap-ში წინასწარ გამზადებული ვებ-გვერდ ელემენტია. [კომპონენტების დოკუმენტაციაში](https://getbootstrap.com/docs/4.5/components/) ნათლად არის თითოეული კომპონენტის გამოყენების ინსტრუქცია, დემონსტრაცია და კოდი განთავსებული,
რომელიც პირდაპირ შეგიძლია გადაწერო პროექტში, გააკეთო მასში ცვლილებები და მოარგო ვებ გვერდს.

### კონტეინერი

კონტეინერში შეგვიძლია მოვათავსოთ ნებისმიერი სახის კონტენტი. Bootstrap-ი მას ავტომატურად აძლევს ჩარჩოს, გამოყოფს გვერდიდნ
და ხდის რესფონსივს ეკრანის გაფართოების მიმართ.

```html
<div class="container">
    content
</div>
```

## [ღილაკები](https://getbootstrap.com/docs/4.5/components/buttons/)
Bootstrap-ში უამრავი სხვადასხვა ტიპისა და ვიზუალის ღილაკია მოთავსებული. დოკუმენტაციაში ნაჩვენები მაგალითებიდან
შეგიძლია აირჩიო სასურველი ღილაკის სტილი და მიუთითო მისი კლასი შენს მიერ გამოყენებულ ღილაკს. მაგალითად:

```html
<button type="button" class="btn btn-success">Success</button>
```

## (Jumbotron)(https://getbootstrap.com/docs/4.5/components/jumbotron/)
ჯამბოტრონი გამოიყენება როგორც "შოუქეის" შეტყობინება ვებ გვერდზე. ეს კომპონენტი წარმოადგენს ერთგვარ ჰაილაითერ ბარათს,
რომელიც მომხმარებელს აწვდის მოკლე შეტყობინებას რესურსზე. მაგალითად:

```html
<div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
  <hr class="my-4">
  <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
  <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
</div>
```

