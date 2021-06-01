import logo from "./logo.svg";
import "./App.css";
import { Component } from "react";
import axios from "axios";
import UsersList from './components/UsersList'

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
    };
  }

  getUsers() {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then((res) => {
        this.setState({ users: res.data.data.users });
      })
      // .then((res)=>{
      //   console.log(res.data.data);
        
      // })
      .catch((err) => {
        console.log(err);
      });
  }
  componentDidMount() {
    this.getUsers();
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-4">
            <br />
            <h1>All Users</h1>
            <hr />
            <br />
             <UsersList users={this.state.users}></UsersList>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
