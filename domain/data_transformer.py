from domain.models import TelemetryData ,DetectionResult,FlightCommand ,GPSData
import time

class DataTransformer:

    def __init__(self):
        
        # gyroscope ayarı şuan da 16384 de ama donanım da farklı bir hassasiyet değeri kullanacaksak değiştirmeliyiz
        self.gyro_const = 16384

    
    def transform_gyro(self, ham_x, ham_y, ham_z):
     
     # Sensör den gelen ham sayıları gerçek açı değerine dönüştürüyoruz ki anlamlı olsun
     aci_x = ham_x / self.gyro_const
     aci_y = ham_y / self.gyro_const
     aci_z = ham_z / self.gyro_const


     # Eğer açı çok küçükse onu 0 kabul edilecek
     if abs(aci_x) < 0.01: 
         aci_x = 0.0
     if abs(aci_y) < 0.01: 
         aci_y = 0.0
     if abs(aci_z) < 0.01:
         aci_z = 0.0
    

     # Ham veriden dönüştürülen gerçek veri değerlerini ataması yapılır
     return TelemetryData(
        roll = aci_x,   # Sağa (+) / Sola (-) yatış
        pitch = aci_y,  # Öne (+) / Arkaya (-) yatış
        yaw = aci_z     # Kendi etrafında sağa/sola dönüş
     )     
    
    def transform_detection(self, label, confidence, bbox, distance):
       
        # AI'dan gelen ham verileri  DetectionResult kutusuna ekliyoruz
        
        return DetectionResult(
            label = label,
            confidence = confidence,
            bbox = bbox,
            distance = distance
        )

   
    def transform_command(self, action, direction, risk_score):
        
        # Karar mekanizmasından gelen emirleri FlightCommand kutusuna ekler
        
        return FlightCommand(
            action = action,
            direction = direction,
            risk_score = risk_score
        )  
        
    def transform_detection(self, label, confidence, bbox, distance):
        
        #mesafe negatifse umursamaz
        if distance < 0:
            distance = 0.0
            
        # sesin tam olarak ne oldugunu nalmadıgında belirsiz girecek
        if confidence < 0.3:
            label = "Unknown/Low_Confidence"

        return DetectionResult(
            label = label,
            confidence = confidence,
            bbox = bbox,
            distance = distance,
            timestamp = time.time() 
        )  
    
    def transform_gps(self, lat, lon, alt):
        
        #GPS uydusundan gelen ham koordinatları (Enlem, Boylam, İrtifa) 
        
        
        return GPSData(
            latitude = lat,   # Kuzey/Güney koordinatı
            longitude = lon,  # Doğu/Batı koordinatı
            altitude = alt,   # Deniz seviyesinden yükseklik
            timestamp = time.time()
        )    
        
    
    
# gyro nun hassasiyeti değişebilir donanım da kontrol edilecek
#donanım kısmında gyroscope sensörü önemli