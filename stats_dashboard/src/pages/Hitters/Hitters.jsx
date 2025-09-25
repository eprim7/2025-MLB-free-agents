import Header from "../../Components/Header/Header";
import HitterStats from "../../Components/HittersStats/HittersStats";
import styles from '../Hitters/Hitters.module.css'
function Hitters(){

    return(
        <>
            <Header />
            <h1>Ranking Hitters</h1>
            <HitterStats />
        </>

    )
}

export default Hitters
