import Navbar from "./components/Navbar";
import Home from "./components/Home";
import axios from "axios";
import React, { Component } from 'react'


const api=axios.create({
  baseURL:"http://127.0.0.1:5100"
}
)

export default class App extends Component {
  state={
    projects=[
    ]
  }

  constructor(){
    super();
    api.get("/").then(
      res => {
        console.log(res)
        this.setState({})
      }
    )
  }
  render() {
    return (
      <div>
        
      </div>
    )
  }
}


export default App;
