# Practice steps
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
## Step 3: test the render function