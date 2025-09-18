import styles from '../Home/Home.module.css'
import Header from '../../Components/Header/Header';

function Home(){
    return(
        <>
        <Header />
        <h1 className={styles.title}>MLB Free Agent Ranker</h1>
        
        <div className={styles.imageContainer}>
        </div>

        <div className={styles.infoContainer}>
            <div className={styles.scrollText}>
                <h2>What</h2>
                <p>
                    A system to rank the upcoming MLB Free Agent class to give
                    coaches, scouts, and front offices a better understanding of the impact of potential 
                    roster additions
                </p>
            </div>
            <div className={styles.scrollText}>
                <h2>Why</h2>
                <p>
                    I wanted to get hands on experience using Python to rank players
                    players, as well as get a greater understanding in general of the upcoming
                    MLB free agent class
                </p>
            </div>
            <div className={styles.scrollText}>
                <h2>How</h2>
                <p>
                    These stats were scraped from multiple sites, as well as pulling data from baseball reference
                    and baseball savant
                </p>
            </div>
        </div>
        
        </>
    )
}

export default Home;
