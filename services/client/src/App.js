import logo from "./logo.svg";
import "./App.css";
import { Component } from "react";
import axios from "axios";
import UsersList from "./components/UsersList";
import AddUser from "./components/AddUser";
class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
      username: '',
      email: '',
    };
    this.addUser = this.addUser.bind(this);
  }

  addUser(event) {
    event.preventDefault();
    console.log("sanity check!");
    console.log(this);
    
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
            <AddUser addUser={this.addUser}
                // username={this.state.username}
                // email={this.state.email}
            />
            <br />
            <UsersList users={this.state.users}></UsersList>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
