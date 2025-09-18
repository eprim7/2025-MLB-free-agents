import styles from '../Header/Header.module.css'
import { Link } from "react-router-dom";

function Header(){
    return(
        <>
            <div className={styles.container}>
                <h1>
                    <Link to="/" className={styles.link}>Home</Link>
                </h1>                
                <h1>
                    <Link to="/pitchers" className={styles.link}>Pitchers</Link>
                </h1>
                <h1>
                    <Link to="/hitters" className={styles.link}>Hitters</Link>
                </h1>
            </div>
        </>
    )
}

export default Header