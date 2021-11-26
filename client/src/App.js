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
    projects=[]
  }

  constructor(){
    super();
    api.get("/").then(
      res => {
        console.log(res.data)
        this.setState({
          projects:res.data
        })
      }
    )
  }

  createCourse = async ()=>{
    let res = await api.post(
      "/",
      {
        id:4,
        title:"test"

      }
    )
    console.log(res)
  }

  render() {
    return (
      <div>
         {this.state.projects.map(
           project => {
             <h2 key={project.id}>{project.title}</h2>
           }
         )}
      </div>
    )
  }
}


export default App;
