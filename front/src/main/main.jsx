import React from "react";
import styles from './main.module.css';
import Button from "../ui-elements/button/button";
import { Link } from "react-router-dom";


function LeftDiv() {
    return (
        <div className={styles.leftDiv}>
            <div className={styles.outside}>
                <div className={styles.header}>Создавай</div>
                <div className={styles.text}>
                    Введите нужные параметры и&nbsp;наш сервис
                    автоматически создаст подходящие вам тесты из&nbsp;уникальных задач
                </div>
                <Link to='/create'>
                    <Button shadow="shadow" size='big' title='Начать' />
                </Link>
            </div>
        </div>
    )
}

function RightDiv() {
    return (
        <div className={styles.rightDiv}>
        </div>
    )
}

const Main = (props) => {

    return (
        <div className={styles.flex}>
            <LeftDiv />
            <RightDiv />
        </div>
    );
}

export default Main;