<script setup>
</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <div id = "banner">

    <div id="pageTitle">
      <h1 id="text">ClubNav</h1>
    </div>
            
    <div id = "searchbar">
      <input type="text" id="myFilter" class="form-control" onkeyup="myFunction()" placeholder="Search Clubs">
    </div>

    <div id="logo">
      <img id="logoImg" src='https://www.d128.org/files/theme%20files/lhslogo-2.png'>
    </div>

  </div>
</template>

<style scoped>
body {
    background-color: grey;
}

h1{
    color: black;
    text-align:center;
    font-family:monospace;
}

#banner {
    width:100%;
    height:15%;
    display: flex;
    align-items: center;
    background-color:#F7E0C4;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#searchDown{
    width:80%;
    height:100%;
    display:flex;
    flex-direction:column;
}

#topMid{
    height:25%;
    display:flex;
    justify-content:center;
    align-items: center;
    
}

#searchContainer{
    display:flex;
    align-items: center;
    justify-content: center;
    background-color: C15700;
    padding:15px;
    border-bottom: lightgray 1px solid;
}
#searchbar {
    display: flex;
    align-self: center;
    justify-content: center;
}


#mid{
    width:100%;
    display:flex;
}
#suggestedBackground {
    width:150px;
    height:47px;
    background-color: aqua;
}

#suggestedOne {
    display:block;
    color:black;
    font-size: 20px;
    text-align:center;
    padding:12px 16px;
    text-decoration: none;
}

#suggestedOne:hover{
    background-color:white;
}

#alphabeticalList{
    width: 40rem;
    clear:both;
}

.alphListBack{
    margin:0;
    padding:0;
    overflow:hidden;
    background-color:transparent;
    width:40rem;
}

li a{
    float:none;
    display:block;
    color:black;
    text-align:left;
    padding:12px 16px;
    text-decoration: none;
}

li a:hover{
    background-color:lightgrey;
}

.cardOne{
    text-decoration: none;
    margin-top: 40px;
    margin-left: 30px;
    display: flex;
    align-content: center;
    width: 300px;
    height: 400px;
    border-radius: 10px;
    flex-direction: column;
    box-shadow: 5px 5px 15px gray;
}

#bottomMid{
    display:flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
}

#myFilter{
    width: 400px;
    height: 50px;
    border-radius: 8px;
    padding: 5px;

}
.imageHolder{
    height:200px;
    display: flex;
}
.card-img-top{
    overflow:hidden;
    object-fit: cover;
    object-position: left top;
}


#filter{
    display:flex;
    flex-direction: column;
    height:100%;

}

.filterItem{
    height:50px;
    display:flex;
}

.filterCheck{
  width:20%;
  display:flex;
  align-items: center;
  justify-content: center;
  
}

.filterTitle{
    width:80%;
    display: flex;
    align-items: center;
    padding: 5px;
}

.realCheck{
    width:20px;
    height: 20px;
}

#text{
    color:black;
    font-size: 96px;
}

#sidebar{
    display: flex;
    padding-top: 30px;
    padding-left: 0px;
}

#logo{
    position:absolute;
    left: 50px;
    top:50px;
}

#pageTitle{
    display: flex;
    justify-content: center;
    width: 100%;
}

#logoImg{
    width:450px;
}

</style>
