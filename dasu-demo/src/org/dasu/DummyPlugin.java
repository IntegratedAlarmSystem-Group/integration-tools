package org.dasu;


import java.util.Scanner;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

import org.eso.ias.plugin.Plugin;
import org.eso.ias.plugin.PluginException;
import org.eso.ias.plugin.config.PluginConfig;
import org.eso.ias.plugin.config.Value;
import org.eso.ias.plugin.publisher.MonitorPointSender;
import org.eso.ias.plugin.publisher.PublisherException;
import org.eso.ias.plugin.publisher.impl.KafkaPublisher;
import org.eso.ias.prototype.input.java.OperationalMode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * publishes data from a weather station to a Kafka Queue
 */
public class DummyPlugin extends Plugin {

    /**
     * runs the plugin.
     *
     * @param args .
     */
    public static void main(String[] args) {
        logger.info("Started...");

        // configuration
        PluginConfig config = new PluginConfig();
        config.setId("DummyPlugin");
        config.setMonitoredSystemId("Terminal values");
        config.setSinkServer("localhost");
        config.setSinkPort(9092);

        Value dummyVal = new Value();
        dummyVal.setId(valueId);
        dummyVal.setRefreshTime(3000);
        config.setValues(new Value[]{dummyVal});

        KafkaPublisher kafkaPublisher = new KafkaPublisher(config.getId(),
                config.getMonitoredSystemId(),
                config.getSinkServer(),
                config.getSinkPort(),
                Plugin.getScheduledExecutorService());

        DummyPlugin dummy = new DummyPlugin(config, kafkaPublisher);

        try {
            dummy.start();
        } catch (PublisherException pe) {
            logger.error("The plugin failed to start", pe);
            System.exit(-3);
        }

        // Connect to the weather station.
        dummy.initialize();
        dummy.setPluginOperationalMode(OperationalMode.OPERATIONAL);

        // This method exits when the user presses CTRL+C
        dummy.startLoop();


        // start reading values from input
        Scanner in = new Scanner(System.in);
        while (in.hasNextDouble()) {
            dummy.value = in.nextDouble();
            logger.info("value updated to " + dummy.value);
        }


        in.close();
        try {
            dummy.loopFuture.get();
        } catch (Exception ce) {
            logger.info("loop terminated");
        }
    }

    /**
     * The logger.
     */
    private static final Logger logger = LoggerFactory.getLogger(DummyPlugin.class);

    /**
     * the loop to keep the plugin running.
     */
    private ScheduledFuture<?> loopFuture;


    private static String valueId = "dummy";
    private Double value = 0.;


    /**
     * Constructor
     *
     * @param config The configuration of the plugin.
     * @param sender The sender.
     */
    private DummyPlugin(PluginConfig config, MonitorPointSender sender) {
        super(config, sender);
    }

    /**
     * Connect to the Weather Station and add the shutdown hook.
     */
    private void initialize() {
        // Adds the shutdown hook
        Runtime.getRuntime().addShutdownHook(new Thread(this::cleanUp, "Release weather station shutdown hook"));
    }

    /**
     * Terminate the thread that publishes the data and disconnects from the weather station.
     */
    private void cleanUp() {
        if (loopFuture != null) {
            loopFuture.cancel(false);
        }
    }

    /**
     * Override method to catch the exception and log a message
     * <p>
     * In the example we do not take any special action if the Plugin returns an
     * error when submitting a new value.
     */
    @Override
    public void updateMonitorPointValue(String mPointID, Object value) {
        try {
            super.updateMonitorPointValue(mPointID, value);
        } catch (PluginException pe) {
            logger.error("Error sending {} monitor point to the core of the IAS", mPointID);
        }
    }

    /**
     * The loop to get monitor values from the weather station and send to the core of the IAS.
     */
    private void startLoop() {
        // send data every second.
        loopFuture = getScheduledExecutorService().scheduleAtFixedRate(
                () -> {
                    updateMonitorPointValue(valueId, value);
                }, 0, 2, TimeUnit.SECONDS);
    }
}
