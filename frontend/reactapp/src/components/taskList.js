import React, { useEffect, useState } from 'react';

import axios from 'axios';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button'



const TaskList = () => {

    const URL = "http://127.0.0.1:8000/";

    const [AllData, setAllData] = useState([]);

    // APi Calls

    const spawnTask = (e) => {
        e.preventDefault(); // prevent refrest on press of button
        //this call will spawn a process on server (using celery)
        axios.post(URL, {}).then(function (response) {

        }).catch((err) => console.log(err.message));
    }


    useEffect(() => {
        setInterval(() => {
            // get request to get data from database  
            axios.get(URL).then(function (response) {
                const { data } = response;
                console.log(data);
                setAllData(data);
            }).catch((err) => console.log(err.message));
        }, 3000)
    }, [])

    return (
        <React.Fragment>

            <Button onClick={spawnTask} variant="primary" size="lg" block style={{ width: 700, marginLeft: 300 }}>
                Start Task
            </Button>

            <Table striped bordered hover size="md" variant="dark" style={{ marginTop: 20, width: 700, marginLeft: 300 }}>
                <thead>
                    <tr>
                        <td><b>Task Id</b></td>
                        <td><b>Task Name</b></td>
                        <td><b>Status</b></td>
                    </tr>
                </thead>
                <tbody>
                    {
                        AllData.map((item) => ( 
                        <tr key={item.task_id}>
                            <td>{item.task_id}</td>
                            <td>{item.task_name}</td>
                            <td>{item.task_status}</td>
                        </tr>
                        ))
                    }
                </tbody>
            </Table>
        </React.Fragment>
    )

}

export default TaskList;