## Step 1: test the ajax function
```
function ajax(src){
    // your code here
    return fetch(src)
        .then((response) => {
            return response.json();
        }
        )
        .catch((error) => {
            return `Error: ${error}`;
        } 
        )
}

ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products")
    .then(data=> console.log(data))
```
```
[
  { name: 'Pixel 3', price: 27700, description: '最新的 Google 手機。' },
  { name: 'Chromecast', price: 1500, description: '在大螢幕上播放喜歡的影片。' },
  {
    name: 'Pixel Book',
    price: 12000,
    description: '最新的 Chromebook 產品。'
  }
]
```

## Step 2: set up html & CSS files
## Step 3: the render function
### create header columns for the table
```
function render(data){
    ......
    const sectionTable = document.querySelector(".table");
    // first make header for each column
    const table = document.createElement('thead')
    const thead = document.createElement('thead');
    const header = document.createElement('tr');
    ['Name', 'Price', 'Description'].forEach(headerText => {
        const columnName = document.createElement('th');
        columnName.textContent = headerText;
    });
    thead.appendChild(header);
    table.appendChild(thead); //table now have header
    ......
```
###
```
function render(data){
    ......
    // then append the contents into table
    const tbody = document.createElement('tbody');
    data.forEach(items => { //get dict
        const row = document.createElement('tr'); // tr for each row
        Object.values(items).forEach(text => {
            const cell = document.createElement('td'); // td for each element
            cell.textContent = text;
            row.appendChild(cell);
        });
        tbody.appendChild(row);
    }) //contents completed
    table.appendChild(tbody); //contents append to table
    sectionTable.appendChild(table); //table appends into <section> part
    ......
}

```
## Step 4: use the callback function render() in the ajax function
```
function ajax(src, callback){
    return fetch(src)
        .then((response) => {
            return response.json();
        })
        .then(data => {
            callback(data);
        })
        .catch((error) => {
            return `Error: ${error}`;
        })
}

#use the ajax function
ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
    function(response){
        render(response);
    }
); // you should get product information in JSON format and render data in the page
```
