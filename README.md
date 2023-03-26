# dronematics

### Monitor drones in real time
- Health
- Flying in authorized fly zone outside of class B , C  and D ![check this image ](doc/images/airspace_classes_large_0.jpeg)

### Tasks 
- [ ] Build Drone data gen simulator
  - [Take Data open data set from this link](https://www.kaggle.com/datasets/kmader/drone-videos?resource=download&select=DJI_0501.SRT)  
  - [To analyze above dataset](https://djitelemetryoverlay.com/srt-viewer/)
- [ ] Kafka
  - [ ] Configure Kafka topic
- [ ] PySpark
  - [ ] Configure pyspark to consume messages
- [ ] Build basic Dash board to work  

### Logical Architecture
```mermaid
    C4Context
      title dronematics Logical Architecture
      Enterprise_Boundary(b0, "BankBoundary0") {
        System(dronA0, "Drone  A0", "A drone on flight")
        System(dronB0, "Drone B0","A drone on flight")
        System_Ext(dronC0, "An external Drone C", "desc")

        Boundary(b1, "Stream Processing") {
          System(SystemAA, "Kafka", "Takes heavy pipe of stream")
          SystemQueue(SystemS, "Stream processing", "Take messages from Kafka and proecess it")
        }
        Boundary(b3, "Dashboard", "boundary") {
            System(SystemDD, "Dashboard", "Presents data")
            
        }
      }

      BiRel(dronA0, SystemAA, "Uses")
      Rel(SystemAA, SystemS, "Consumer", "Telematic Messages")
      Rel(SystemS, SystemDD, "Status", "Either status or Alert")



      UpdateRelStyle(dronA0, SystemAA, $textColor="blue", $lineColor="blue", $offsetX="5")
      UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")

```

