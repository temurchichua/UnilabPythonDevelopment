[<img align="left" width="100" src="https://i.pinimg.com/originals/71/4c/2a/714c2a88445cae52454a5b31c668445e.png">](https://i.pinimg.com/originals/71/4c/2a/714c2a88445cae52454a5b31c668445e.png)
[<img align="right" width="150" src="https://github.com/firstcontributions/first-contributions/raw/master/assets/join-slack-team.png">](https://join.slack.com/t/unilabpythond-h2d3773/shared_invite/zt-h5gvz8mb-dNnD33Wn88TN9jqgHsuOcQ)

# სავარჯიშო რეპოზიტორია
ეს არის Unilab-ის პითონის NLP-ზე მომუშავე გუნდის სავარჯიშო რეპოზიტორია. რეპოზიტორიას გამოვიყენებთ მანამ სანამ არ გადავალთ უშუალოდ პროექტის შექმნისთვის საჭირო სამუშაოებზე.

#### *თუ ჯერ-ჯერობით გიტის ტერმინალ გარემოს არ იცნობთ, [აქ შეგიძლიათ ნახოთ ყველაზე ხშირად გამოყენებადი კომანდები]( #https://education.github.com/git-cheat-sheet-education.pdf )*

<img align="right" width="300" src="https://github.com/firstcontributions/first-contributions/blob/master/assets/fork.png" alt="fork this repository" />

თუ გიტი ჯერ კიდევ არ დაგიყენებიათ მოწყობილობაზე, [გადმოწერეთ და დააინსტალირეთ ამ მისამართიდან]( https://help.github.com/articles/set-up-git/).

## Fork this repository
პროექტზე კოლექტიურად სამუშაოდ დაფორკეთ ეს რეპოზიტორია. ამისთვის დააჭირეთ fork ღილაკს გვერდის ზედა მარჯვენა ზოლში.
ამ რიგად თქვენს ანგარიშზე გაჩნდება რეპოზიტორიის ასლი.

## Clone the repository

<img align="right" width="300" src="https://github.com/firstcontributions/first-contributions/blob/master/assets/clone.png" alt="clone this repository" />

საკუთარ ანგარიშზე გაჩენილი დაფორკილი რეპოზიტორია გადაიტანეთ/დაკლონეთ თქვენს მოწყობილობაში. ამისთვის თქვენს ანგარიშზე გახსენით დაფორკილი რეპოზიტორია, დააჭირეთ clone ღილაკს და *copy to clipboard* იკონს.

თქვენს სამუშაო გარემოში გახსენით ტერმინალი და ჩააკოპირეთ შემდეგი გიტ კომანდი:

```
git clone <მისამართი რომელიც დააკოპირეთ კლონირებისთვის>
```
"<>"- სიმბოლოების წაშლით და ქლიფბორდში დაკოპირებული მისამართის ჩასმით მიიღებთ ბრძანების საბოლოო სახეს.

<img align="right" width="300" src="https://github.com/firstcontributions/first-contributions/blob/master/assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

მაგალითისთვის, თქვენგან დაფორკილ ამ რეპოზიტორიის მისამართს ექნება შემდეგნაირი სახე:
```
git clone https://github.com/this-is-you/firstrepo.git
```
სადაც `this-is-you` არის თქვენი GitHub username. ამ რიგად თქვენ აკოპირებთ პირველი რეპოზიტორიის თქვენ მიერ დაფორკილ ვერსიას
სამუშაო მოწყობილობაზე.

## Create a branch

იმისთვის რომ უკეთ ჩასწვდეთ ბრენჩის როლს და მნიშვნელობას, [გაეცანით ოფიციალურ დოკუმენტაციას Branch თემაზე](https://github.com/firstcontributions/first-contributions/blob/master/).

სამუშაო გარემოში, ტერმინალი გადაიყვანეთ გადმოწერილი რეპოზიტორიის დირექტორიაში/საქაღალდის მისამართზე.

იმ შემთხვევაში თუ უკვე იქ არ იმყოფებით, გამოიყენეთ შემდეგი ბრძანება:

```
cd firstrepo
```
ახლა კი შევქმნათ ახალი ტოტი/branch `git checkout` ბრძანების გამოყენებით:
```
git checkout -b <add-your-new-branch-name>
```

სადაც `add-your-new-branch-name` შეიძლება იყოს ნებისმიერი სახელი, რომლითაც ტოტზე შესასრულებელ სამუშაოს ლაკონურად აღწერთ, მაგალითად:
```
git checkout -b adding-my-code
```


## გავავკეთოთ პროექტში ცვლილება და დავაკომიტოთ სამუშაოს დასრულებისას

მას შემდეგ რაც გაამზადებთ პროექტს თქვენს მოწყობილობაში, დაამატეთ დირექტორიას თქვენი კოდი და პროექტის აღწერა /firstProjects საქაღალდეში საკუთარი საქაღალდის შექმნით. საქაღალდის დასახელება '''/სახელი_გვარი''' ფორმატით გაამზადეთ, ხოლო ფაილები: `readme.md`, `app.py` დასახელებებით. 

<img align="right" width="450" src="https://github.com/firstcontributions/first-contributions/blob/master/assets/git-status.png" alt="git status" />


If you go to the project directory and execute the command `git status`, you'll see there are changes.


Add those changes to the branch you just created using the `git add` command:

```
git add Contributors.md
```

Now commit those changes using the `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
replacing `<your-name>` with your name.

## Push changes to GitHub

Push your changes using the command `git push`:
```
git push origin <add-your-branch-name>
```
replacing `<add-your-branch-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a  `Compare & pull request` button. Click on that button.

<img style="float: right;" src="https://github.com/firstcontributions/first-contributions/blob/master/assets/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://github.com/firstcontributions/first-contributions/blob/master/assets/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats!  You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

You could join our slack team in case you need any help or have any questions. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)


## Tutorials Using Other Tools

| <a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GitHub Desktop](github-desktop-tutorial.md)                 | [Visual Studio 2017](github-windows-vs2017-tutorial.md)      | [GitKraken](gitkraken-tutorial.md)                           | [Visual Studio Code](github-windows-vs-code-tutorial.md)     | [Atlassian Sourcetree](sourcetree-macos-tutorial.md)         | [IntelliJ IDEA](github-windows-intellij-tutorial.md)         |
