import React from "react";
import Rodal from "rodal";
import {
  GiBackstab,
  GiSandsOfTime,
  GiCardJoker,
  GiTrophy,
} from "react-icons/gi";
import "rodal/lib/rodal.css";
import "./rodal.scss";
import history from "../../history";
import { Button } from "..";

const MAX_TIME = 10;

const BootstrapModal = (props) => {
  return (
    <Rodal
      {...props}
      closeOnEsc={false}
      closeMaskOnClick={false}
      showCloseButton={false}
      className="rodal__container"
      height={100 - props.time > 80 ? 400 : 310}
    >
      <div className="rodal__title">Game Over</div>
      <div className="rodal__content">
        <div>
          {props.victory ? (
            <>
              {" "}
              <GiTrophy /> YOU WIN!!{" "}
            </>
          ) : (
            <>
              {" "}
              <GiBackstab /> YOU LOSE!!{" "}
            </>
          )}{" "}
        </div>
        <div>
          <GiSandsOfTime /> Time Taken: {MAX_TIME - props.time} sec
        </div>
        <div>
          <GiCardJoker /> Cards Flipped: {props.flips}
        </div>
      </div>
      {MAX_TIME == MAX_TIME - props.time && parseInt(props.flips) < 16 ? (
        <div className="rodal__discrepancy_container">
          <p
            style={{
              textAlign: "center",
            }}
          >
            You haven't played properly, Play again please 😭
          </p>
        </div>
      ) : MAX_TIME - props.time < 30 ? (
        <div className="rodal__discrepancy_container">
          <p
            style={{
              textAlign: "center",
            }}
          >
            Fast memory like a bullet
          </p>
        </div>
      ) : MAX_TIME - props.time > 30 && MAX_TIME - props.time < 100 ? (
        <div className="rodal__discrepancy_container">
          <p
            style={{
              textAlign: "center",
            }}
          >
            Very fast!
          </p>
        </div>
      ) : (
        MAX_TIME - props.time > 100 && (
          <div className="rodal__discrepancy_container">
            <p
              style={{
                textAlign: "center",
              }}
            >
              You have a memory discrepancy, please upload your MRI scan for
              further analysis
            </p>
          </div>
        )
      )}
      <div className="rodal__btn-container">
        <Button marginTop="1rem" onClick={() => history.push("/theme")}>
          Back
        </Button>
        <Button onClick={() => props.onPlayAgain()}>Play again</Button>
      </div>
    </Rodal>
  );
};

export default BootstrapModal;
